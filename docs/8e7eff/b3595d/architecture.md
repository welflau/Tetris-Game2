# 架构设计 - 核心玩法机制设计文档

## 架构模式
MVC + 状态机模式

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: HTML5 Canvas + 自定义游戏引擎
- **database**: LocalStorage/IndexedDB
- **others**: Web Audio API, RequestAnimationFrame, ES6 Modules

## 模块设计

### TetrominoGenerator
职责: 负责方块生成逻辑，实现7-bag随机算法，确保方块分布均匀
- generateNext()
- getPreview()
- reset()

### GameBoard
职责: 管理游戏网格状态，处理方块放置、行消除检测和网格更新
- placeTetromino()
- checkLines()
- clearLines()
- isValidPosition()

### TetrominoController
职责: 控制当前方块的移动、旋转、下落逻辑和碰撞检测
- move()
- rotate()
- drop()
- checkCollision()

### ScoreSystem
职责: 计算分数、等级、消除行数统计，实现标准计分规则
- addScore()
- updateLevel()
- getStats()

### DifficultyManager
职责: 根据等级调整下落速度，管理难度递增曲线
- getDropSpeed()
- updateDifficulty()
- getLevelThreshold()

### GameStateManager
职责: 管理游戏状态（开始、暂停、结束），处理状态转换
- start()
- pause()
- gameOver()
- reset()

### InputHandler
职责: 处理键盘输入，实现按键映射和输入缓冲
- bindKeys()
- handleInput()
- setKeyRepeat()

## 数据流
用户输入 -> InputHandler -> TetrominoController -> GameBoard -> ScoreSystem -> DifficultyManager -> 渲染更新。TetrominoGenerator独立生成方块序列，GameStateManager协调整体流程

## 风险点
- 方块旋转边界检测复杂性
- 高速下落时的碰撞检测精度
- 多行同时消除的动画同步
- 不同设备的帧率差异影响游戏体验

## 关键决策
- 采用SRS旋转系统确保标准化体验
- 使用7-bag算法平衡随机性和公平性
- 实现软降和硬降双重下落机制
- 基于标准NES版本的计分和等级系统
- 使用状态机模式管理复杂的游戏状态转换
