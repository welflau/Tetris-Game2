# 架构设计 - 设计游戏架构和核心类结构

## 架构模式
MVC + 状态机模式

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: HTML5 Canvas / WebGL
- **database**: LocalStorage（存储游戏记录）
- **others**: requestAnimationFrame, 事件监听器, 状态管理模式

## 模块设计

### Game（游戏控制器）
职责: 游戏主循环控制、状态管理、用户输入处理、渲染协调
- start(): void - 开始游戏
- pause(): void - 暂停游戏
- resume(): void - 恢复游戏
- gameLoop(): void - 游戏主循环
- handleInput(key: string): void - 处理用户输入
- update(deltaTime: number): void - 更新游戏状态
- render(): void - 渲染游戏画面

### Grid（游戏网格）
职责: 管理10x20游戏网格、检测碰撞、处理行消除、存储已固定方块
- isValidPosition(block: Block, x: number, y: number): boolean - 检测位置是否有效
- placeBlock(block: Block): void - 放置方块到网格
- checkLines(): number[] - 检测完整行
- clearLines(lines: number[]): number - 清除完整行并返回消除行数
- isGameOver(): boolean - 检测游戏是否结束
- getCell(x: number, y: number): number - 获取网格单元状态

### Block（方块类）
职责: 定义方块形状、旋转状态、位置信息、移动逻辑
- constructor(type: BlockType, x: number, y: number) - 构造函数
- rotate(): void - 旋转方块
- move(dx: number, dy: number): void - 移动方块
- getShape(): number[][] - 获取当前形状矩阵
- getPosition(): {x: number, y: number} - 获取位置
- clone(): Block - 克隆方块对象

### BlockFactory（方块工厂）
职责: 生成随机方块、管理方块类型定义、预览下一个方块
- createRandomBlock(): Block - 创建随机方块
- createBlock(type: BlockType): Block - 创建指定类型方块
- getNextBlock(): Block - 获取下一个方块预览
- getBlockShapes(): Map<BlockType, number[][][]> - 获取所有方块形状定义

### GameState（游戏状态）
职责: 管理游戏状态、分数、等级、统计信息
- getScore(): number - 获取分数
- getLevel(): number - 获取等级
- getLinesCleared(): number - 获取消除行数
- updateScore(lines: number): void - 更新分数
- getState(): GameStateEnum - 获取游戏状态
- setState(state: GameStateEnum): void - 设置游戏状态

### InputManager（输入管理器）
职责: 处理键盘输入、输入映射、防抖处理
- bindEvents(): void - 绑定键盘事件
- unbindEvents(): void - 解绑事件
- isKeyPressed(key: string): boolean - 检测按键状态
- setKeyHandler(key: string, handler: Function): void - 设置按键处理函数

### Renderer（渲染器）
职责: 游戏画面渲染、UI绘制、动画效果
- renderGrid(grid: Grid): void - 渲染游戏网格
- renderBlock(block: Block): void - 渲染当前方块
- renderUI(gameState: GameState): void - 渲染UI信息
- renderNextBlock(block: Block): void - 渲染下一个方块预览
- clear(): void - 清空画布

## 数据流
用户输入 -> InputManager -> Game控制器 -> 更新Block位置/状态 -> Grid碰撞检测 -> 更新GameState -> Renderer渲染 -> 显示到Canvas。游戏主循环通过requestAnimationFrame驱动，每帧检查方块下落、用户输入、碰撞检测、行消除等逻辑。

## 风险点
- 旋转碰撞检测复杂，需要处理边界情况
- 60fps性能要求，需要优化渲染和计算逻辑
- 方块形状定义和旋转状态管理容易出错
- 游戏状态同步可能导致显示不一致

## 关键决策
- 采用MVC架构分离游戏逻辑、数据和渲染
- 使用状态机模式管理游戏状态转换
- 方块用二维数组表示，支持4个旋转状态
- 使用工厂模式生成方块，便于扩展新类型
- 采用Canvas 2D渲染，平衡性能和开发复杂度
- 使用requestAnimationFrame确保60fps流畅度
