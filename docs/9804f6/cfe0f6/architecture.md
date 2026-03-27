# 架构设计 - 搭建项目基础架构和游戏循环系统

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Canvas
- **database**: localStorage（本地存储）
- **others**: CSS3, Webpack（可选）, ESLint, Prettier

## 模块设计

### GameEngine
职责: 游戏主循环控制器，管理游戏状态、帧率控制和模块协调
- start()
- pause()
- resume()
- stop()
- update(deltaTime)
- render()

### RenderEngine
职责: Canvas渲染引擎，负责所有图形绘制和视觉效果
- init(canvas)
- clear()
- drawGrid()
- drawTetromino()
- drawUI()
- resize()

### InputManager
职责: 输入事件处理器，管理键盘输入和事件分发
- init()
- bindEvents()
- getInputState()
- onKeyDown()
- onKeyUp()

### GameBoard
职责: 游戏棋盘数据模型，维护10x20网格状态
- init()
- getCell(x, y)
- setCell(x, y, value)
- clearRow(row)
- isRowFull(row)

### Tetromino
职责: 方块数据模型和操作逻辑
- create(type)
- move(dx, dy)
- rotate()
- getShape()
- getPosition()

### CollisionDetector
职责: 碰撞检测系统，验证方块移动和旋转的有效性
- checkCollision(tetromino, board)
- isValidPosition(x, y, shape)
- checkBounds()

### ScoreManager
职责: 分数和等级管理系统
- addScore(lines)
- updateLevel()
- getScore()
- getLevel()
- getLinesCleared()

### UIManager
职责: 用户界面管理器，处理UI元素显示和更新
- init()
- updateScore()
- updateLevel()
- showNextPiece()
- showGameOver()

## 数据流
InputManager捕获用户输入 -> GameEngine处理游戏逻辑更新 -> Tetromino和GameBoard更新状态 -> CollisionDetector验证操作有效性 -> ScoreManager计算分数 -> RenderEngine绘制画面 -> UIManager更新界面元素

## 风险点
- Canvas在不同设备上的性能差异可能影响60FPS目标
- 键盘事件处理的浏览器兼容性问题
- requestAnimationFrame的时间精度可能不够稳定
- 移动端触摸控制需要额外适配

## 关键决策
- 采用requestAnimationFrame而非setInterval确保流畅的60FPS
- 使用模块化设计便于后续功能扩展和维护
- Canvas 2D Context足够满足俄罗斯方块的渲染需求
- 采用事件驱动架构处理用户输入和游戏状态变化
- 使用TypeScript类型定义提高代码质量（可选）
- 实现响应式Canvas尺寸适配不同屏幕
