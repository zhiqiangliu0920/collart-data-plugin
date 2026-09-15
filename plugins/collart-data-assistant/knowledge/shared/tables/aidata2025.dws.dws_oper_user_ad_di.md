---
id: "table:aidata2025.dws.dws_oper_user_ad_di"
title: "aidata2025.dws.dws_oper_user_ad_di · 用户粒度广告收入表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dws.dws_oper_user_ad_di.md", "dataform:aidata/definitions/dws/daily/h_dws_oper_user_ad_di.sqlx", "feishu:aidata2025.dws.dws_oper_user_ad_di", "schema:aidata2025.dws.dws_oper_user_ad_di"]
tags: ["dws_oper_user_ad_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_oper_user_ad_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dws.dws_oper_user_ad_di · 用户粒度广告收入表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_oper_user_ad_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | schema |
| `user_pseudo_id` | STRING | NULLABLE | 用户id，firebase分配的唯一id | 飞书 |
| `user_id` | STRING | NULLABLE | 用户id，内部平台分配的唯一id | 飞书 |
| `atlasv_uid` | STRING | NULLABLE | 技术团队给用户定义的唯一id | 飞书 |
| `unit_id` | STRING | NULLABLE | 广告位 | schema |
| `placement` | STRING | NULLABLE | 广告场景 | schema |
| `country` | STRING | NULLABLE | 国家 | schema |
| `app_name` | STRING | NULLABLE | app名 | schema |
| `package_name` | STRING | NULLABLE | 包名 | schema |
| `traffic_src_name` | STRING | NULLABLE | 渠道名称 | schema |
| `traffic_src_type` | STRING | NULLABLE | 渠道类型 | schema |
| `app_version` | STRING | NULLABLE | 版本 | schema |
| `is_new` | BOOLEAN | NULLABLE | 是否新用户 | schema |
| `is_active` | BOOLEAN | NULLABLE | 是否活跃 | schema |
| `vip_type` | STRING | NULLABLE | 是否订阅 | schema |
| `ad_type` | STRING | NULLABLE | 广告类型 | schema |
| `device_language` | STRING | NULLABLE | 设备语言 | schema |
| `mobile_brand_name` | STRING | NULLABLE | 设备品牌名 | 飞书 |
| `mobile_model_name` | STRING | NULLABLE | 设备型号 | 飞书 |
| `device_total_ram` | STRING | NULLABLE | 设备内存 | 飞书 |
| `ad_sdk_init_cnt` | INTEGER | NULLABLE | 广告sdk启动次数 | schema |
| `ad_load_cnt` | INTEGER | NULLABLE | 广告请求次数 | schema |
| `ad_load_success_cnt` | INTEGER | NULLABLE | 广告请求成功次数 | schema |
| `ad_load_fail_cnt` | INTEGER | NULLABLE | 广告请求失败次数 | schema |
| `ad_load_duration` | FLOAT | NULLABLE | 加载时长 | schema |
| `ad_start_to_show_cnt` | INTEGER | NULLABLE | 到达广告场景准备展示次数 | schema |
| `ad_success_to_show_cnt` | INTEGER | NULLABLE | 达到广告场景可展示次数 | schema |
| `ad_show_cnt` | INTEGER | NULLABLE | 广告填充成功后自动调show次数 | schema |
| `ad_impression_cnt` | INTEGER | NULLABLE | 广告展示次数 | schema |
| `ad_impression_fail_cnt` | INTEGER | NULLABLE | 广告展示失败次数 | schema |
| `ad_click_cnt` | INTEGER | NULLABLE | 广告点击次数 | schema |
| `ad_close_cnt` | INTEGER | NULLABLE | 广告关闭次数 | schema |
| `ad_duration` | FLOAT | NULLABLE | 广告时长 | schema |
| `ad_value` | FLOAT | NULLABLE | 广告价值 | schema |
| `adjust_id` | STRING | NULLABLE | adjust id | 飞书 |
| `advertising_id` | STRING | NULLABLE | 广告id | schema |

## 定义差异与补充

- unit_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- unit_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- placement: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- placement: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- traffic_src_name: 飞书补充解释：投放渠道名称
- traffic_src_name: 旧文档补充解释：投放渠道名称
- traffic_src_type: 飞书补充解释：投放渠道类型
- traffic_src_type: 旧文档补充解释：投放渠道类型
- app_version: 飞书补充解释：app客户端版本号
- app_version: 旧文档补充解释：app客户端版本号
- is_new: 飞书补充解释：是否新老用户，true代表新用户、false代表老用户
- is_new: 旧文档补充解释：是否新老用户，true代表新用户、false代表老用户
- is_active: 飞书补充解释：布尔标记字段，用于表示是/否状态。
- is_active: 旧文档补充解释：布尔标记字段，用于表示是/否状态。
- vip_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- vip_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- ad_sdk_init_cnt: 飞书补充解释：广告sdk初始化次数
- ad_sdk_init_cnt: 旧文档补充解释：广告sdk初始化次数
- ad_load_cnt: 飞书补充解释：广告加载次数
- ad_load_cnt: 旧文档补充解释：广告加载次数
- ad_load_success_cnt: 飞书补充解释：广告加载成功次数
- ad_load_success_cnt: 旧文档补充解释：广告加载成功次数
- ad_load_fail_cnt: 飞书补充解释：广告加载失败次数
- ad_load_fail_cnt: 旧文档补充解释：广告加载失败次数
- ad_load_duration: 飞书补充解释：广告加载时长
- ad_load_duration: 旧文档补充解释：广告加载时长
- ad_start_to_show_cnt: 飞书补充解释：广告准备展示次数
- ad_start_to_show_cnt: 旧文档补充解释：广告准备展示次数
- ad_success_to_show_cnt: 飞书补充解释：广告成功展示次数
- ad_success_to_show_cnt: 旧文档补充解释：广告成功展示次数
- ad_show_cnt: 飞书补充解释：广告展示次数
- ad_show_cnt: 旧文档补充解释：广告展示次数
- ad_value: 飞书补充解释：广告价值，客户端埋点统计
- ad_value: 旧文档补充解释：广告价值，客户端埋点统计
- advertising_id: 飞书补充解释：用户的广告id身份，也是一种唯一id
- advertising_id: 旧文档补充解释：用户的广告id身份，也是一种唯一id

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_user_event_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdws!3sdws_oper_user_ad_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdws%2Fdaily%2Fh_dws_oper_user_ad_di.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dws/daily/h_dws_oper_user_ad_di.sqlx`；仓库 `aidata`，路径 `definitions/dws/daily/h_dws_oper_user_ad_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:55.037408+00:00`。同一 SQLX 的产出：`aidata2025.dws.dws_oper_user_ad_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
AND event_name IN ('ad_sdk_init',
INNER JOIN (
AND to_date ) b
AND a.event_date=b.event_date
AND a.package_name=b.package_name;
```

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_oper_user_event_di
