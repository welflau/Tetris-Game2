# 架构设计 - 消行系统与计分机制开发

## 架构模式
模块化MVC架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas

## 模块设计

### LineDetector
职责: 检测游戏区域中的满行，返回满行索引数组
- detectFullLines(gameBoard)
- isLineFull(line)
- getFullLineIndices(gameBoard)

### LineClearSystem
职责: 处理消行逻辑，包括行移除和上方行下移
- clearLines(gameBoard, lineIndices)
- removeLines(gameBoard, lineIndices)
- dropLinesAbove(gameBoard, clearedLines)

### ScoreSystem
职责: 计分系统，根据消行数量计算分数和等级
- calculateScore(linesCleared, level)
- updateLevel(totalLines)
- getScoreMultiplier(linesCleared)
- saveHighScore(score)

### ClearAnimation
职责: 消行动画效果，提供视觉反馈
- playLineClearAnimation(lineIndices)
- highlightLines(lineIndices)
- fadeOutLines(lineIndices, callback)

### GameStats
职责: 游戏统计数据管理，包括分数、等级、消行数
- updateStats(linesCleared)
- getStats()
- resetStats()
- saveToLocalStorage()

## 数据流
游戏主循环检测到方块落地后，LineDetector扫描游戏区域找出满行 -> LineClearSystem执行消行逻辑并更新游戏区域 -> ClearAnimation播放消行动画 -> ScoreSystem计算分数和等级更新 -> GameStats更新统计数据并保存到LocalStorage -> 触发UI更新显示新的分数和等级

## 关键决策
- 采用事件驱动模式，消行完成后触发分数更新事件
- 使用Promise处理消行动画，确保动画完成后再继续游戏逻辑
- 实现标准俄罗斯方块计分规则：单行100分，双行300分，三行500分，四行800分
- 等级系统每10行提升一级，影响方块下落速度
- 消行动画使用Canvas渐变效果，持续时间300ms
- 统计数据实时保存到LocalStorage，支持游戏重启后恢复
