# 架构设计 - Tetromino方块系统开发

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### TetrominoFactory
职责: 负责创建和管理7种Tetromino方块类型的工厂类
- createTetromino(type): Tetromino
- getRandomTetromino(): Tetromino
- getAllTypes(): Array<string>

### Tetromino
职责: 单个方块的数据结构和基础操作
- rotate(direction): void
- getShape(): Array<Array<number>>
- getPosition(): {x: number, y: number}
- setPosition(x, y): void
- clone(): Tetromino

### TetrominoRenderer
职责: 负责方块的Canvas渲染和视觉效果
- render(tetromino, context): void
- renderPreview(tetromino, context): void
- renderGhost(tetromino, context): void

### RotationSystem
职责: 实现SRS旋转系统，处理旋转逻辑和碰撞修正
- rotate(tetromino, direction, gameBoard): boolean
- getWallKickData(type, rotation): Array<{x, y}>
- validateRotation(shape, position, gameBoard): boolean

### TetrominoQueue
职责: 管理方块队列，实现7-bag随机生成算法
- getNext(): Tetromino
- peek(count): Array<Tetromino>
- refillBag(): void

## 数据流
TetrominoQueue生成方块序列 -> TetrominoFactory创建具体方块实例 -> Tetromino存储方块状态和形状数据 -> RotationSystem处理旋转变换 -> TetrominoRenderer将方块渲染到Canvas -> 游戏主循环更新方块位置和状态

## 风险点
- 旋转系统的SRS算法实现复杂度较高
- Canvas渲染性能优化需要精细调试
- 方块旋转时的边界检测和碰撞处理逻辑复杂
- 不同方块类型的旋转中心点计算可能出错

## 关键决策
- 采用标准SRS旋转系统确保游戏体验符合现代俄罗斯方块标准
- 使用7-bag随机算法保证方块分布的公平性
- 方块数据使用二维数组表示，便于旋转和碰撞检测
- 分离渲染逻辑和游戏逻辑，提高代码可维护性
- 使用工厂模式管理方块创建，便于扩展新的方块类型
