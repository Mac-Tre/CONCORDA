import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import Ajv2020 from "ajv/dist/2020.js";
import addFormats from "ajv-formats";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const load = name => JSON.parse(fs.readFileSync(path.join(root,name),"utf8"));
const schemas = ["conversation_artifact","conflict_classification","memory_update","rose_mirror_report"].map(name => load("schemas/"+name+".schema.json"));
const ajv = new Ajv2020({allErrors:true,strict:false});
addFormats(ajv);
for (const schema of schemas) ajv.addSchema(schema, schema.$id);
const validate = (schemaName, data) => {
  const schema = schemas.find(s => s.title === schemaName);
  if (!schema) throw new Error("Missing schema "+schemaName);
  const fn = ajv.getSchema(schema.$id);
  if (!fn(data)) throw new Error(schemaName+" invalid: "+ajv.errorsText(fn.errors));
};

export function verifyDemo(artifact, expected) {
  validate("Conversation Artifact",artifact);
  validate("Conflict Classification",expected.conflict_classification);
  validate("Rose Mirror Report",expected.rose_mirror_report);
  if(artifact.source_type !== "synthetic_fixture" || artifact.redaction_status !== "synthetic_redacted") {
    throw new Error("Demo only accepts synthetic redacted fixtures");
  }
  if(expected.rose_mirror_report.participant_id !== "participant_a") throw new Error("Unexpected report recipient");
  if(expected.rose_mirror_report.memory_recommendations.some(m=>m.approved || !m.requires_consent)) {
    throw new Error("Memory must remain unapproved without consent");
  }
  const flags=expected.conflict_classification.safety_flags;
  if(flags.length>0 && expected.conflict_classification.repair_coaching_allowed) {
    throw new Error("Safety flags must disable repair coaching");
  }
  if(flags.length>0 && expected.rose_mirror_report.next_best_message) {
    throw new Error("No repair message permitted for safety-flagged inputs");
  }
  const forbidden = ["relationship_health_score","partner_b_private_read","private_partner_b","hidden vulnerability"];
  const text = JSON.stringify(expected.rose_mirror_report).toLowerCase();
  if(forbidden.some(v=>text.includes(v))) throw new Error("Forbidden field or content in participant report");
  return true;
}

const escapeHtml = text => String(text).replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
export function renderReport(report) {
  const entries = [
    ["Private Read",report.private_read],["Strongest Point",report.strongest_point],
    ["Growth Edge",report.growth_edge],["Constructive Challenge",report.constructive_challenge.stronger_replacement_behavior],
    ["Next Best Message",report.next_best_message],["Daily Practice",report.daily_practice],
    ["Bottom Line",report.bottom_line]
  ];
  const cards=entries.map(([k,v])=>'<section><h2>'+escapeHtml(k)+'</h2><p>'+escapeHtml(v??"")+'</p></section>').join("");
  return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rose Mirror — synthetic demonstration</title><style>body{margin:0;background:#F7F4EE;color:#24364C;font:16px/1.55 system-ui}main{max-width:720px;margin:auto;padding:28px}header{border-left:6px solid #5FA9A2;padding-left:18px}section{margin:15px 0;padding:20px;border-radius:14px;background:white}h2{font-size:18px;margin:0 0 6px}p{margin:0}.notice{color:#7b3f34}</style><main><header><h1>Rose Mirror™</h1><p class="notice">Synthetic fixture demo · Not a live AI analysis, therapy, diagnosis or safety assessment</p></header>'+cards+'</main></html>';
}
export function runDemo() {
  const artifact=load("fixtures/trial_run_gray_input.redacted.json");
  const expected=load("fixtures/trial_run_gray_expected_output.json");
  verifyDemo(artifact,expected);
  if(process.argv.includes("--validate-only")) { console.log("Synthetic fixture and expected report validated");return; }
  const folder=path.join(root,"demo");
  fs.mkdirSync(folder,{recursive:true});
  fs.writeFileSync(path.join(folder,"rose-mirror-preview.json"),JSON.stringify(expected.rose_mirror_report,null,2)+"\n");
  fs.writeFileSync(path.join(folder,"rose-mirror-preview.html"),renderReport(expected.rose_mirror_report));
  console.log("Generated synthetic preview in demo/ (not a live inference pipeline)");
}
if(process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url)) runDemo();
