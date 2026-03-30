# 架构设计 - Tetromino方块系统开发

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Canvas
- **database**: LocalStorage
- **others**: CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### TetrominoFactory
职责: 负责创建和管理7种Tetromino方块类型的定义和实例化
- createTetromino(type): Tetromino
- getRandomTetromino(): Tetromino
- getAllTypes(): Array<string>

### Tetromino
职责: 单个方块的数据模型，包含形状、颜色、位置、旋转状态
- rotate(): void
- move(dx, dy): void
- getShape(): Array<Array<number>>
- getPosition(): {x, y}
- clone(): Tetromino

### TetrominoRenderer
职责: 负责方块的Canvas渲染，包括主游戏区域和预览区域
- renderTetromino(tetromino, context, offsetX, offsetY): void
- renderGhost(tetromino, context, ghostY): void
- clearBlock(context, x, y): void

### ShapeDefinitions
职责: 存储7种方块的形状定义、颜色配置和旋转矩阵
- getShapeData(type): Object
- getRotationStates(type): Array<Array<Array<number>>>
- getColor(type): string

### TetrominoController
职责: 处理方块的用户输入控制和游戏逻辑交互
- handleInput(keyCode): void
- updatePosition(): void
- checkCollision(tetromino, board): boolean

## 数据流
ShapeDefinitions提供方块定义 -> TetrominoFactory根据定义创建Tetromino实例 -> TetrominoController处理用户输入更新方块状态 -> TetrominoRenderer将方块渲染到Canvas -> 游戏主循环通过requestAnimationFrame持续更新

## 风险点
- 方块旋转时的边界检测复杂性
- Canvas渲染性能优化挑战
- 不同方块类型的碰撞检测准确性
- 旋转算法的数学计算复杂度

## 关键决策
- 使用工厂模式创建方块实例，便于扩展新方块类型
- 采用二维数组表示方块形状，简化碰撞检测算法
- 分离渲染逻辑和游戏逻辑，提高代码可维护性
- 使用Canvas离屏渲染技术优化性能
- 实现方块的不可变性，通过克隆避免状态污染
