# 架构设计 - 消行系统和计分系统

## 架构模式
MVC模式 + 观察者模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3 Animation, Web Audio API, requestAnimationFrame

## 模块设计

### LineDetector
职责: 检测游戏区域中的满行，返回需要消除的行索引
- detectFullLines(gameBoard)
- isLineFull(lineArray)

### LineClearAnimator
职责: 处理消行的视觉动画效果，包括闪烁、淡出等
- playLineClearAnimation(lineIndexes)
- onAnimationComplete(callback)

### ScoreCalculator
职责: 根据消行数量、当前等级计算分数，实现计分规则
- calculateScore(linesCleared, level)
- getScoreMultiplier(linesCleared)

### LevelManager
职责: 管理游戏等级，控制下落速度，处理等级提升逻辑
- updateLevel(totalLinesCleared)
- getDropSpeed(level)
- checkLevelUp()

### GameStats
职责: 统计和存储游戏数据，包括分数、等级、消行数等
- updateStats(score, lines, level)
- saveToStorage()
- loadFromStorage()

### LineClearController
职责: 协调消行流程，整合检测、动画、计分和数据更新
- processLineClear(gameBoard)
- onLineClearComplete()

## 数据流
游戏循环检测满行 -> LineDetector识别满行索引 -> LineClearAnimator播放消除动画 -> 同时ScoreCalculator计算得分 -> LevelManager检查等级提升 -> GameStats更新统计数据 -> 通知UI更新显示 -> 继续游戏循环

## 风险点
- 动画播放期间的游戏状态管理复杂性
- 多行同时消除时的性能优化
- 计分规则的平衡性调整
- Canvas重绘频率对性能的影响

## 关键决策
- 使用观察者模式解耦消行事件和UI更新
- 采用CSS3动画配合Canvas实现流畅的消行效果
- 实现经典俄罗斯方块计分规则：单行100分，双行300分，三行500分，四行800分
- 每消除10行提升一个等级，等级影响下落速度
- 使用requestAnimationFrame确保动画流畅性
