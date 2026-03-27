# 架构设计 - 核心玩法机制设计

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: HTML5 Canvas + 原生JS
- **database**: LocalStorage (本地存储)
- **others**: CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### TetrominoFactory
职责: 管理7种俄罗斯方块类型的定义、生成和属性
- createTetromino(type): Tetromino
- getRandomTetromino(): Tetromino
- getAllTetrominoTypes(): Array

### GameBoard
职责: 游戏棋盘状态管理、碰撞检测、行消除逻辑
- isValidPosition(tetromino, x, y): boolean
- placeTetromino(tetromino, x, y): void
- clearFullLines(): number
- getBoard(): Array

### MovementController
职责: 处理方块移动、旋转、下落的核心逻辑
- moveLeft(): boolean
- moveRight(): boolean
- rotate(): boolean
- softDrop(): boolean
- hardDrop(): void

### ScoreSystem
职责: 计分系统、等级管理、下落速度控制
- addScore(lines, level): void
- updateLevel(): void
- getDropSpeed(): number
- getGameStats(): Object

### GameEngine
职责: 游戏主循环、状态管理、事件协调
- start(): void
- pause(): void
- gameLoop(): void
- handleInput(key): void

## 数据流
用户输入 -> MovementController -> GameBoard碰撞检测 -> 有效移动更新方块位置 -> GameBoard检查消除 -> ScoreSystem更新分数 -> GameEngine更新游戏状态 -> 渲染器更新显示

## 风险点
- 旋转算法复杂度较高，需要处理边界情况
- 消除动画可能影响游戏流畅度
- 高速下落时的碰撞检测精度问题
- 不同浏览器的Canvas性能差异

## 关键决策
- 采用标准SRS旋转系统确保游戏体验一致性
- 使用二维数组表示游戏棋盘，便于碰撞检测和渲染
- 实现T-Spin等高级玩法以增加游戏深度
- 分离游戏逻辑和渲染逻辑，便于测试和维护
- 使用状态机管理游戏不同阶段（开始、游戏中、暂停、结束）
