# 架构设计 - 实现7种方块类型和基础图形系统

## 架构模式
MVC + 模块化组件架构

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生HTML5 Canvas + CSS3
- **database**: LocalStorage (本地存储)
- **others**: HTML5, CSS3, Canvas 2D API, Web Audio API

## 模块设计

### TetrominoShapes
职责: 定义7种方块类型的形状数据和旋转状态
- getShape(type, rotation)
- getAllShapes()
- getRandomShape()

### Tetromino
职责: 方块实例类，管理单个方块的状态和行为
- move(dx, dy)
- rotate()
- getPosition()
- getShape()
- clone()

### GameBoard
职责: 游戏棋盘管理，处理方块放置和行消除
- isValidPosition(tetromino)
- placeTetromino(tetromino)
- clearLines()
- getBoard()

### Renderer
职责: 图形渲染系统，负责绘制游戏界面
- drawBoard()
- drawTetromino(tetromino)
- drawUI()
- clear()

### InputController
职责: 用户输入处理，键盘和触摸事件管理
- bindEvents()
- handleKeyPress(event)
- handleTouch(event)

### GameEngine
职责: 游戏主循环和状态管理
- start()
- pause()
- reset()
- update()
- gameLoop()

### ScoreManager
职责: 计分系统和游戏统计
- addScore(lines)
- getScore()
- getLevel()
- saveHighScore()

### AudioManager
职责: 音效和背景音乐管理
- playSound(type)
- playMusic()
- setVolume(level)
- mute()

## 数据流
用户输入 -> InputController -> GameEngine -> 更新Tetromino和GameBoard状态 -> Renderer渲染 -> ScoreManager更新分数 -> AudioManager播放音效 -> 循环继续

## 风险点
- Canvas渲染性能在低端设备上可能不佳
- 不同浏览器的键盘事件处理差异
- 移动端触摸操作体验优化挑战
- 方块旋转边界检测的复杂性

## 关键决策
- 使用原生Canvas而非WebGL以确保广泛兼容性
- 采用二维数组表示方块形状，便于旋转计算
- 实现标准SRS旋转系统确保游戏体验
- 使用requestAnimationFrame实现流畅的游戏循环
- 模块化设计便于后续功能扩展和维护
