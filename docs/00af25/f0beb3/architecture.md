# 架构设计 - 设计文档整合与输出

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生HTML5 Canvas + Web APIs
- **database**: LocalStorage (本地存储)
- **others**: CSS3, Web Audio API, RequestAnimationFrame, Webpack/Vite (构建工具)

## 模块设计

### GameEngine (游戏引擎)
职责: 管理游戏主循环、状态机、时间控制和整体游戏流程
- start()
- pause()
- resume()
- reset()
- update(deltaTime)
- render()

### GameBoard (游戏面板)
职责: 管理游戏网格、方块放置、行消除逻辑和碰撞检测
- placeTetromino()
- clearLines()
- checkCollision()
- isGameOver()

### Tetromino (俄罗斯方块)
职责: 定义方块类型、形状、旋转逻辑和移动行为
- rotate()
- move(direction)
- getShape()
- getPosition()

### InputController (输入控制器)
职责: 处理键盘、触摸输入事件，转换为游戏指令
- bindEvents()
- handleKeyPress()
- handleTouch()
- getInputState()

### ScoreManager (计分管理器)
职责: 管理分数计算、等级提升、统计数据和排行榜
- addScore(lines)
- updateLevel()
- getHighScore()
- saveScore()

### Renderer (渲染器)
职责: 负责Canvas绘制、动画效果、UI渲染和视觉反馈
- drawBoard()
- drawTetromino()
- drawUI()
- playAnimation()

### AudioManager (音频管理器)
职责: 管理背景音乐、音效播放和音频设置
- playBGM()
- playSFX()
- setVolume()
- mute()

### StorageManager (存储管理器)
职责: 处理游戏数据持久化、设置保存和读取
- saveGame()
- loadGame()
- saveSettings()
- getHighScores()

## 数据流
用户输入 → InputController → GameEngine → GameBoard/Tetromino → ScoreManager → Renderer → Canvas显示。游戏状态通过事件系统在各模块间传递，Renderer订阅状态变化进行重绘，StorageManager负责数据持久化。

## 风险点
- Canvas性能优化挑战，特别是在低端设备上的流畅度
- 移动端触控操作体验设计复杂度
- 游戏平衡性调试需要大量测试时间
- 跨浏览器兼容性问题，特别是音频API支持
- 实时游戏循环的精确时间控制实现难度

## 关键决策
- 选择原生Canvas而非WebGL，降低复杂度并确保广泛兼容性
- 采用组件化架构便于功能扩展和维护
- 使用LocalStorage而非服务器存储，简化部署和隐私保护
- 实现响应式设计支持多设备，优先移动端体验
- 采用状态机模式管理游戏状态转换
- 使用RequestAnimationFrame确保流畅的60FPS渲染
