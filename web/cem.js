import { app } from '../../scripts/app.js'
import * as root from "./mod_methods/root.js";

const MOD_METHODS = {
  ...root
}

app.registerExtension({
  name: "cem_tools",
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    MOD_METHODS[nodeData.name]?.beforeDef?.(nodeType, nodeData, app)
  },
  nodeCreated(node, app) {
    MOD_METHODS[node.comfyClass]?.whenCreated?.(node, app)
  }
})
