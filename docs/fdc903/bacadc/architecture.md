# 架构设计 - 实现游戏状态管理系统

## 架构模式
状态机模式 + MVC架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: HTML5 Canvas + 原生JS
- **database**: LocalStorage（本地存储游戏状态）
- **others**: 状态机库, 事件系统, 定时器管理

## 模块设计

### GameStateManager
职责: 管理游戏的各种状态（MENU、PLAYING、PAUSED、GAME_OVER）及状态间的转换逻辑
- setState(state)
- getCurrentState()
- canTransition(fromState, toState)
- onStateChange(callback)

### GameController
职责: 处理游戏控制逻辑，响应用户输入，协调各模块工作
- start()
- pause()
- resume()
- restart()
- handleInput(keyCode)
- update(deltaTime)

### GameOverDetector
职责: 检测游戏结束条件，包括方块堆积到顶部的判断
- checkGameOver(grid, newBlock)
- isTopRowBlocked(grid)
- canPlaceBlock(grid, block)

### ScoreManager
职责: 管理游戏分数、等级、消除行数等统计信息
- addScore(lines)
- getScore()
- getLevel()
- getLinesCleared()
- reset()

### InputHandler
职责: 处理键盘输入，根据当前游戏状态分发不同的控制命令
- bindKeys()
- handleKeyDown(event)
- handleKeyUp(event)
- setInputEnabled(enabled)

### GameLoop
职责: 管理游戏主循环，控制帧率和游戏更新频率
- start()
- stop()
- pause()
- resume()
- setFPS(fps)
- addUpdateCallback(callback)

### UIRenderer
职责: 渲染游戏界面，包括游戏状态提示、分数显示、暂停界面等
- renderGameState(state)
- renderScore(score)
- renderPauseScreen()
- renderGameOverScreen()

## 数据流
用户输入 -> InputHandler -> GameController -> GameStateManager -> 状态变更 -> 通知各模块 -> GameLoop驱动更新 -> Grid/Block更新 -> GameOverDetector检测 -> ScoreManager更新分数 -> UIRenderer渲染界面

## 风险点
- 状态转换逻辑复杂，可能出现状态不一致
- 游戏结束判断时机不准确，影响用户体验
- 暂停/恢复功能可能导致定时器混乱
- 多个状态同时变更时的竞态条件

## 关键决策
- 采用有限状态机模式管理游戏状态，确保状态转换的可控性
- 使用观察者模式实现状态变更通知，降低模块间耦合
- 游戏结束检测在每次方块放置后立即执行，确保及时响应
- 暂停功能通过停止游戏循环实现，保持游戏状态完整性
- 使用LocalStorage持久化最高分等关键数据
