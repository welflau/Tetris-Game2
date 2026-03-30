# 架构设计 - 游戏引擎核心架构开发

## 架构模式
模块化游戏引擎架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas

## 模块设计

### GameEngine
职责: 游戏引擎核心类，管理游戏循环、状态切换和全局配置
- start()
- pause()
- resume()
- stop()
- setState()
- getState()

### GameLoop
职责: 游戏主循环管理，使用requestAnimationFrame实现60fps渲染
- run()
- pause()
- resume()
- setFPS()
- addUpdateCallback()

### StateManager
职责: 游戏状态管理器，处理菜单、游戏中、暂停、结束等状态
- setState()
- getState()
- onStateChange()
- isState()

### EventSystem
职责: 事件系统，处理键盘输入、游戏事件的发布订阅
- on()
- off()
- emit()
- once()
- removeAllListeners()

### GameBoard
职责: 游戏区域管理，维护10x20网格状态和渲染
- init()
- render()
- getCell()
- setCell()
- clearLine()
- isLineFull()

### CanvasRenderer
职责: Canvas渲染器，优化绘制性能和动画效果
- init()
- clear()
- drawGrid()
- drawBlock()
- drawText()
- resize()

## 数据流
GameEngine作为核心控制器，通过StateManager管理游戏状态，GameLoop驱动每帧更新，EventSystem处理用户输入并触发相应事件，GameBoard维护游戏数据状态，CanvasRenderer负责将数据渲染到Canvas上。数据流向：用户输入 -> EventSystem -> GameEngine -> StateManager -> GameBoard -> CanvasRenderer -> 屏幕显示

## 关键决策
- 采用模块化设计，每个核心组件独立封装便于测试和维护
- 使用requestAnimationFrame替代setInterval实现流畅的60fps游戏循环
- 实现发布订阅模式的事件系统，降低模块间耦合度
- GameBoard使用二维数组存储游戏状态，便于碰撞检测和消行逻辑
- CanvasRenderer采用双缓冲技术优化渲染性能
- 在现有index.html基础上添加Canvas元素和游戏容器，保持现有页面结构
