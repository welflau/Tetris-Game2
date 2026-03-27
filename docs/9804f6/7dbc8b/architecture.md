# 架构设计 - 实现方块数据结构和渲染系统

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Canvas
- **database**: 无（纯前端实现）
- **others**: Canvas 2D API, RequestAnimationFrame, CSS3

## 模块设计

### TetrominoFactory
职责: 定义和创建7种方块类型的数据结构，包括形状矩阵、颜色、旋转状态等
- createTetromino(type)
- getTetrominoData(type)
- getAllTypes()

### TetrominoRenderer
职责: 负责在Canvas上渲染方块，处理颜色填充、边框绘制、位置计算等视觉呈现
- renderTetromino(tetromino, x, y)
- renderGrid()
- clearCanvas()
- setBlockSize()

### Tetromino
职责: 方块实体类，存储单个方块的状态信息（类型、位置、旋转状态、颜色）
- getShape()
- getColor()
- getPosition()
- setPosition(x, y)
- rotate()

### GameBoard
职责: 游戏面板管理，维护10x20网格状态，处理方块在面板上的位置映射
- getCell(x, y)
- setCell(x, y, value)
- clearBoard()
- isValidPosition(tetromino, x, y)

### CanvasManager
职责: Canvas画布管理，处理画布初始化、尺寸调整、坐标转换等底层绘图操作
- initCanvas()
- resizeCanvas()
- getContext()
- coordToPixel(x, y)

## 数据流
TetrominoFactory创建方块数据 -> Tetromino实例存储方块状态 -> GameBoard验证位置有效性 -> TetrominoRenderer在Canvas上绘制 -> CanvasManager处理底层绘图操作

## 风险点
- Canvas性能优化问题，频繁重绘可能影响帧率
- 方块旋转时的边界检测复杂度
- 不同屏幕尺寸下的方块大小适配
- 方块颜色和视觉效果的用户体验

## 关键决策
- 使用二维数组表示方块形状，便于旋转算法实现
- 采用工厂模式创建方块，提高代码复用性
- 使用Canvas 2D API而非WebGL，降低复杂度
- 方块渲染采用分层绘制，先清空再重绘
- 预定义7种方块的4个旋转状态，避免实时计算
