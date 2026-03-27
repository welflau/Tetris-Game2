# 架构设计 - 实现计分和等级系统

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Canvas
- **database**: LocalStorage（本地存储）
- **others**: CSS3, HTML5, RequestAnimationFrame API

## 模块设计

### ScoreManager
职责: 核心计分逻辑管理，包括分数计算、等级提升、统计数据维护
- addScore(linesCleared, level): 根据消除行数和等级计算并添加分数
- updateLevel(): 检查并更新等级
- getScore(): 获取当前分数
- getLevel(): 获取当前等级
- getLines(): 获取总消除行数
- reset(): 重置所有计分数据

### ScoreCalculator
职责: 分数计算算法实现，处理不同消除行数的分数计算和等级倍率
- calculateLineScore(linesCleared): 计算基础行消除分数
- applyLevelMultiplier(baseScore, level): 应用等级倍率
- getSpeedByLevel(level): 根据等级获取下降速度

### UIScoreDisplay
职责: 分数相关UI的渲染和更新，包括分数、等级、行数的实时显示
- updateScore(score): 更新分数显示
- updateLevel(level): 更新等级显示
- updateLines(lines): 更新消除行数显示
- renderScorePanel(): 渲染整个计分面板
- showLevelUpEffect(): 显示升级特效

### GameStatistics
职责: 游戏统计数据管理，包括历史最高分、游戏时长等扩展统计
- updateHighScore(score): 更新最高分记录
- getHighScore(): 获取历史最高分
- saveGameStats(): 保存游戏统计到本地存储
- loadGameStats(): 从本地存储加载统计数据

### LevelSystem
职责: 等级系统逻辑，管理等级提升条件、速度变化和难度调整
- checkLevelUp(totalLines): 检查是否满足升级条件
- calculateDropSpeed(level): 计算当前等级的下降速度
- getLevelThreshold(level): 获取指定等级的升级门槛

## 数据流
游戏主循环检测到行消除事件 → ScoreManager接收消除行数 → ScoreCalculator计算基础分数和等级倍率 → LevelSystem检查等级提升 → ScoreManager更新分数、等级、行数数据 → UIScoreDisplay实时更新界面显示 → GameStatistics更新统计数据并保存到LocalStorage → 将新的等级信息反馈给游戏主循环调整下降速度

## 风险点
- 分数计算精度问题，需要确保大数值计算的准确性
- 等级提升时的速度变化可能影响游戏流畅性
- UI更新频率过高可能影响游戏性能
- LocalStorage存储限制和数据持久化风险

## 关键决策
- 采用经典俄罗斯方块计分规则：单行100分、双行300分、三行500分、四行800分
- 等级系统每10行提升一级，最高等级限制为20级
- 分数倍率公式：baseScore * (level + 1)，确保等级提升有明显收益
- 使用LocalStorage进行本地数据持久化，避免依赖外部数据库
- UI更新采用requestAnimationFrame同步，确保与游戏主循环一致的60FPS
- 等级影响下降速度：speed = Math.max(1, 21 - level) * 50ms
