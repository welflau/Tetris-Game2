# 架构设计 - 排行榜系统开发

## 架构模式
增量模块扩展

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + LocalStorage

## 模块设计

### LeaderboardManager
职责: 排行榜数据管理，包括分数存储、排序、持久化
- saveScore(playerName, score, level, lines)
- getTopScores(limit)
- clearLeaderboard()
- exportScores()
- importScores(data)

### LeaderboardUI
职责: 排行榜界面渲染和交互
- render(container)
- showLeaderboard()
- hideLeaderboard()
- updateDisplay(scores)
- showNewRecordDialog(score)

### ScoreEntry
职责: 新纪录输入界面，处理玩家姓名输入
- showEntryDialog(score, callback)
- validatePlayerName(name)
- submitScore(name, score)

## 数据流
游戏结束时触发分数检查 -> 判断是否为新纪录 -> 显示姓名输入对话框 -> LeaderboardManager保存分数到LocalStorage -> LeaderboardUI更新显示 -> 排行榜按分数降序展示前10名记录

## 关键决策
- 使用LocalStorage作为数据持久化方案，符合项目轻量化要求
- 排行榜数据结构包含：playerName、score、level、lines、timestamp
- 默认显示前10名记录，支持数据导入导出功能
- 集成到现有游戏界面中，作为独立模块可通过按键或菜单调用
- 新纪录检测逻辑集成到游戏结束流程中
- 支持匿名玩家（默认名称：Anonymous Player）
