---
id: "table:aidata2025.dwd.dwd_oper_user_event_di"
title: "aidata2025.dwd.dwd_oper_user_event_di · ai组原始埋点表（轻汇总）"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_oper_user_event_di.md", "dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_event_di-new_app.sqlx", "dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_event_di.sqlx", "feishu:aidata2025.dwd.dwd_oper_user_event_di", "schema:aidata2025.dwd.dwd_oper_user_event_di"]
tags: ["dwd_oper_user_event_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_oper_user_event_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_oper_user_event_di · ai组原始埋点表（轻汇总）

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_oper_user_event_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | app_name, event_name |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `event_name` | STRING | NULLABLE | 事件名/事件英文名 | 飞书 |
| `user_pseudo_id` | STRING | NULLABLE | 用户id，firebase分配的唯一id | 飞书 |
| `user_id` | STRING | NULLABLE | 用户id，内部平台分配的唯一id | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `traffic_src_name` | STRING | NULLABLE | 投放渠道名称 | 飞书 |
| `event_time` | DATETIME | NULLABLE | 事件触发时间 | 飞书 |
| `traffic_src_source` | STRING | NULLABLE | 投放渠道source | 飞书 |
| `traffic_src_type` | STRING | NULLABLE | 投放渠道类型 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `city` | STRING | NULLABLE | 用户所在城市 | 飞书 |
| `device_language` | STRING | NULLABLE | 设备语言 | 飞书 |
| `mobile_brand_name` | STRING | NULLABLE | 设备品牌名 | 飞书 |
| `mobile_model_name` | STRING | NULLABLE | 设备型号 | 飞书 |
| `app_version` | STRING | NULLABLE | app客户端版本号 | 飞书 |
| `install_source` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `install_store` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `device_total_ram` | STRING | NULLABLE | 设备内存 | 飞书 |
| `network_type` | STRING | NULLABLE | 设备网络类型 | 飞书 |
| `device_id` | STRING | NULLABLE | 设备id | 飞书 |
| `is_vip` | STRING | NULLABLE | 是否新老用户，true代表付费用户、false代表免费用户 | 飞书 |
| `is_login` | STRING | NULLABLE | 是否登录用户，true代表登录用户、false代表未登录用户 | 飞书 |
| `vip_product_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_duration` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `ad_type` | STRING | NULLABLE | 广告类型 | 飞书 |
| `event_value` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `unit_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_from` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_placement` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| ` advertising_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_order_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_product_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_temp_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_service_type` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_module_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_module_title` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_module_index` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_feature_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_retouch_feature_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_use_type` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_mode_type` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_is_regenerate` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_generate_cnt` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_auto_optimization` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_motion_mode` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_ratio` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_model` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_page` | STRING | NULLABLE | 事件发生所在页面 | 飞书 |
| `atlasv_uid` | STRING | NULLABLE | 技术团队给用户定义的唯一id | 飞书 |
| `event_model_type` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_credit_count` | INTEGER | NULLABLE | 计数指标字段，用于统计人数、次数或记录量。 | 飞书 |
| `event_service_cost` | FLOAT | NULLABLE | 成本字段，用于记录投放、服务或业务成本。 | 飞书 |
| `mobile_marketing_name` | STRING | NULLABLE | 设备型号 | 飞书 |
| `adjust_id` | STRING | NULLABLE | adjust id | 飞书 |
| `event_engagement_time_msec` | STRING | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `event_source` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_type` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_param_name` | STRING | NULLABLE | 事件参数 | 飞书 |
| `event_sort_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_adjust_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_sc_value` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_vfx_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_filter_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_material_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_textfont_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_textemplate_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_textanime_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_transition_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_group_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_clipanime_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_anime_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_category` | STRING | NULLABLE | 事件类型 | 飞书 |
| `event_project_template` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_unlock_type` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_enter` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_mode` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_modes` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_error_value` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_keyframe` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_mask` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_background` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_chroma_key` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_hsl` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_enhance` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_body_fx` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_time_limit` | STRING | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `event_smooth_slow_motion` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `os_classify` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `os_cpu_info` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `device_operating_system_version` | STRING | NULLABLE | 操作系统版本 | 飞书 |
| `event_feature` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_space_type` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_design_style` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `event_space_name` | STRING | NULLABLE | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `params_is_vip` | STRING | NULLABLE | 是否新老用户，true代表付费用户、false代表免费用户 | 飞书 |
| `params_ad_platform` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `session_id` | STRING | NULLABLE | 会话session_id | schema |
| `keywordID` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `transaction_id` | STRING | NULLABLE | event_param = 'transaction_id'' | schema |
| `device_category` | STRING | NULLABLE | 设备类型，电脑/平板 | 飞书 |
| `operating_system` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `browser` | STRING | NULLABLE | 浏览器类型 | 飞书 |
| `task_id` | STRING | NULLABLE | 模型调用任务id | schema |
| `temp_id` | STRING | NULLABLE | 模版id | schema |
| `fb_campaign` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_page_location` | STRING | NULLABLE | 未说明 | 缺口 |
| `first_open_time` | TIMESTAMP | NULLABLE | 用户首次打开时间 | schema |
| `geo_continent` | STRING | NULLABLE | 大洲 | schema |
| `geo_sub_continent` | STRING | NULLABLE | 次大洲 | schema |
| `device_vendor_id` | STRING | NULLABLE | iOS vendor_id | schema |
| `traffic_src_medium` | STRING | NULLABLE | 归因渠道 medium | schema |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `advertising_id` | string | 用户的广告id身份，也是一种唯一id |

## 定义差异与补充

- event_time: 飞书 类型 timestamp；schema 类型 DATETIME
- event_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- session_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- session_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- transaction_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- transaction_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- task_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- task_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- temp_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- temp_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | storytemplate-10a27.analytics_232977577.events_* |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_user_event_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdwd%2Fdaily%2Fh_dwd_oper_user_event_di.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_event_di-new_app.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_oper_user_event_di-new_app.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:54.609021+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_oper_user_event_di`。
- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_event_di.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_oper_user_event_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:54.563364+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_oper_user_event_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date
and app_name in ('muselab','looksart','VibeDance_iOS','VibeDance_Android','Vidart');
AND FORMAT_DATE('%Y%m%d', to_date)
AND event_name NOT LIKE 'tech%'
AND event_name NOT LIKE 'dev%'
AND event_name NOT IN ('fire_base_start_request',
and ((app_info.id = 'ai.photo.generator.fotos.ai.image.editor.app.free' and app_info.install_source <>'manual_install')
LEFT JOIN UNNEST(ARRAY(SELECT AS STRUCT * FROM dim.dim_product_info)) AS b
ON coalesce(app_info.id,'collart_web') = b.package_name
WHERE user_pseudo_id IS NOT NULL

AND to_date
and app_name not in ('muselab','looksart','VibeDance_iOS','VibeDance_Android','Vidart');
WHERE ( _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', from_date)
AND FORMAT_DATE('%Y%m%d', to_date)
AND CONCAT('intraday_', FORMAT_DATE('%Y%m%d', to_date))
AND event_name NOT LIKE 'tech%'
AND event_name NOT LIKE 'dev%'
AND event_name NOT IN ('fire_base_start_request',
and (app_info.install_source <>'manual_install' or app_info.id is null)
AND app_info.id NOT IN ('com.my.drama.box.reel.short.stream.tv.app')
LEFT JOIN UNNEST(ARRAY(SELECT AS STRUCT * FROM dim.dim_product_info)) AS b
ON coalesce(app_info.id,'collart_web') = b.package_name
WHERE user_pseudo_id IS NOT NULL
```

飞书登记上游（不保证当前依赖）：storytemplate-10a27.analytics_232977577.events_*
- 物理上游：`fx-editor.analytics_263446298.events_*`
- 物理上游：`home-ai-708e3.analytics_495972540.events_intraday_*`
- 物理上游：`muselab-9b0d3.analytics_530699929.events_*`
- 物理上游：`muselab-9b0d3.analytics_530699929.events_intraday_*`
- 物理上游：`photoenhance-5754e.analytics_326551552.events_*`
- 物理上游：`removeobjects-17cd7.analytics_348205064.events_*`
- 物理上游：`removeobjects-17cd7.analytics_348205064.events_intraday_*`
- 物理上游：`speedtest-ios.analytics_152266665.events_*`
- 物理上游：`speedtestlite-ios.analytics_243888008.events_*`
- 物理上游：`storytemplate-10a27.analytics_232977577.events_*`
- 物理上游：`vibedance-540a0.analytics_533044528.events_*`
- 物理上游：`vibedance-540a0.analytics_533044528.events_intraday_*`
- 物理上游：`vidart-8b8ca.analytics_528583115.events_*`
- 物理上游：`vidart-8b8ca.analytics_528583115.events_intraday_*`
