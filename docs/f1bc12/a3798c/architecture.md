# 架构设计 - 游戏引擎核心架构开发

## 架构模式
MVC + 观察者模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage
- **others**: Web Audio API, requestAnimationFrame, CSS3

## 模块设计

### GameEngine
职责: 游戏引擎核心，管理游戏循环、状态切换、全局配置
- start()
- pause()
- resume()
- stop()
- getState()
- setState()

### GameLoop
职责: 游戏主循环控制，使用requestAnimationFrame实现60FPS渲染
- run()
- pause()
- resume()
- setFPS()
- addUpdateCallback()

### StateManager
职责: 游戏状态管理，处理MENU、PLAYING、PAUSED、GAMEOVER等状态
- changeState()
- getCurrentState()
- registerStateHandler()

### EventSystem
职责: 事件系统，实现观察者模式，处理游戏内各种事件通信
- emit()
- on()
- off()
- once()

### InputManager
职责: 输入管理器，处理键盘输入、防抖、按键映射
- bindKey()
- unbindKey()
- isPressed()
- enableDebounce()

### Renderer
职责: 渲染引擎，管理Canvas绘制、动画效果、UI元素渲染
- render()
- clear()
- drawGrid()
- drawTetromino()
- drawUI()

### GameBoard
职责: 游戏区域模型，维护10x20网格状态、碰撞检测
- getCell()
- setCell()
- isValidPosition()
- clearLines()

### TetrominoFactory
职责: 方块工厂，生成7种Tetromino类型，管理方块队列
- createTetromino()
- getNext()
- getPreview()

## 数据流
用户输入 -> InputManager -> EventSystem -> GameEngine -> StateManager -> GameLoop -> 业务逻辑更新 -> Renderer -> Canvas显示。事件系统作为中央总线，各模块通过事件进行解耦通信。

## 风险点
- Canvas渲染性能在低端设备上可能不佳
- requestAnimationFrame在后台标签页会暂停，需要处理页面可见性
- 键盘事件在不同浏览器的兼容性问题
- 游戏循环时间精度可能影响游戏体验

## 关键决策
- 采用MVC架构分离游戏逻辑、数据和视图
- 使用观察者模式实现模块间解耦通信
- 选择requestAnimationFrame而非setInterval确保流畅动画
- 使用单例模式管理全局游戏引擎实例
- 采用工厂模式生成Tetromino方块对象
- 使用状态机模式管理游戏不同阶段
