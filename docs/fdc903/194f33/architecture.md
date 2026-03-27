# 架构设计 - 实现游戏主循环和渲染系统

## 架构模式
MVC + 游戏循环架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: HTML5 Canvas + 原生JS
- **database**: LocalStorage（游戏状态持久化）
- **others**: requestAnimationFrame, 事件监听器, 定时器

## 模块设计

### GameLoop
职责: 管理60fps主循环，协调更新和渲染时序
- start()
- stop()
- pause()
- resume()
- setFPS(fps)

### Renderer
职责: 负责所有游戏元素的绘制和视觉效果
- render(gameState)
- drawGrid()
- drawBlock(block)
- drawUI()
- clear()

### InputManager
职责: 处理键盘输入事件并转换为游戏指令
- bindEvents()
- handleKeyDown(event)
- handleKeyUp(event)
- getInputState()

### GameController
职责: 协调各模块，管理游戏状态流转
- init()
- update(deltaTime)
- handleInput()
- onGameOver()
- reset()

### TimeManager
职责: 管理游戏时间，控制方块下落速度和动画
- getDeltaTime()
- updateDropTimer()
- shouldDrop()
- setDropSpeed(speed)

### AnimationSystem
职责: 处理行消除动画、方块移动过渡效果
- playLineAnimation(lines)
- playDropAnimation()
- update(deltaTime)
- isPlaying()

## 数据流
InputManager捕获用户输入 -> GameController处理游戏逻辑更新 -> Game/Grid/Block模型状态变更 -> Renderer根据最新状态绘制画面 -> GameLoop通过requestAnimationFrame循环执行

## 风险点
- 60fps性能优化挑战，需要避免频繁的DOM操作
- 输入延迟可能影响游戏体验
- 动画效果与游戏逻辑同步复杂度
- 不同浏览器的requestAnimationFrame兼容性

## 关键决策
- 使用requestAnimationFrame而非setInterval确保流畅渲染
- 采用双缓冲技术避免画面闪烁
- 输入事件采用状态机模式处理连续按键
- 游戏逻辑与渲染分离，支持可变时间步长
- 使用Canvas 2D API而非WebGL降低复杂度
