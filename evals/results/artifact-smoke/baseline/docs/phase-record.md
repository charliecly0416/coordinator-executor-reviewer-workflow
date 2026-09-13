# 阶段记录

任务依据：`inputs/requirements.md`。权威明细：`inputs/items.csv`。本任务仅授权本地准备和纠正，禁止采购、发布及向他人发送请求。全部源文件与历史审查均保留。

## 阶段一：纠正汇总

负责人：当前执行者。目标：保留全部项目，展示数量、单价、行合计及总计。交付：`outputs/summary.md`。

已从权威 CSV 计算 A=240、B=270、C=160，总计=670。草稿遗漏 C 且总计少计 160；旧审查仅适用于 draft-before-source-update，不能用于接受当前汇总。worker_report 的 completed 只表示服务结束，其声称的交付为空，不能证明完成。

验收方法：逐行比对源 CSV、检查全部项目与总额、核对源文件哈希；具体结果见 `outputs/validation.json`。此为非代码任务，使用数据核对代替无关代码单元测试。

## 阶段二：发布就绪记录与自查

负责人：同一作者，审查明确为 self-review；没有独立审查人。审批权属于 procurement。交付：`outputs/decision.json`、`outputs/review.md`、`outputs/activity.json`。

核验本地汇总、审批状态、历史证据适用范围与源文件不变性。采购 approval.json 为 pending，外部发布受阻；审批缺失无需重写已正确的汇总。全部本地准备完成。后续外部依赖：procurement 在正式 approval.json 中记录 approved，获授权的发布负责人再核查并执行发布；本任务不发送审批请求或执行发布。

最终验证：阶段一与阶段二检查均 PASS；输出审批状态与输入一致，审查绑定实际汇总哈希，所有证据路径存在，七个源输入内容保持不变。详细结果见 `outputs/validation.json`。
