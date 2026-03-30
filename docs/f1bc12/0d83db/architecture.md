# 架构设计 - 游戏状态管理与暂停功能

## 架构模式
状态机模式 + 观察者模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript
- **database**: LocalStorage
- **others**: HTML5 Canvas, CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### GameStateManager
职责: 管理游戏的各种状态（运行、暂停、结束、菜单等）和状态转换
- setState(state)
- getState()
- canTransition(fromState, toState)
- onStateChange(callback)

### PauseController
职责: 处理暂停相关的逻辑，包括暂停界面显示、快捷键处理、暂停时的游戏保存
- pause()
- resume()
- toggle()
- isPaused()
- saveGameState()

### GameLifecycleManager
职责: 管理游戏的生命周期，包括开始、重新开始、结束等操作
- startGame()
- restartGame()
- endGame()
- resetGame()

### StateEventDispatcher
职责: 状态变化事件的分发和通知，实现观察者模式
- subscribe(event, callback)
- unsubscribe(event, callback)
- dispatch(event, data)

### UIStateController
职责: 根据游戏状态更新UI界面，包括暂停遮罩、按钮状态、菜单显示等
- updateUI(state)
- showPauseOverlay()
- hidePauseOverlay()
- updateButtons(state)

### InputStateFilter
职责: 根据当前游戏状态过滤和处理输入事件
- filterInput(input, state)
- enableInput()
- disableInput()
- registerStateInput(state, handler)

## 数据流
用户触发暂停 -> InputStateFilter过滤输入 -> PauseController处理暂停逻辑 -> GameStateManager更新状态 -> StateEventDispatcher分发状态变化事件 -> UIStateController更新界面 -> 游戏引擎暂停/恢复渲染循环

## 风险点
- 状态转换逻辑复杂，可能出现状态不一致
- 暂停时需要正确保存游戏状态，避免数据丢失
- 多个状态监听器可能导致性能问题
- 暂停界面的层级管理可能与游戏渲染冲突

## 关键决策
- 采用状态机模式确保状态转换的安全性和可预测性
- 使用观察者模式实现松耦合的状态变化通知
- 暂停时保存完整游戏状态到内存，避免频繁LocalStorage操作
- 使用CSS层级和Canvas暂停渲染相结合的方式实现暂停界面
- 实现防抖机制避免快速按键导致的状态混乱
