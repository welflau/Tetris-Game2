# 架构设计 - 游戏状态管理系统

## 架构模式
状态机模式 + 观察者模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript
- **database**: LocalStorage
- **others**: HTML5 Canvas, CSS3, Web Audio API, requestAnimationFrame

## 模块设计

### GameStateManager
职责: 管理游戏状态转换，维护状态机逻辑
- setState(state): 设置游戏状态
- getState(): 获取当前状态
- canTransition(fromState, toState): 验证状态转换
- onStateChange(callback): 注册状态变化监听器

### GameController
职责: 协调各个游戏组件，处理状态变化时的业务逻辑
- startGame(): 开始游戏
- pauseGame(): 暂停游戏
- resumeGame(): 继续游戏
- endGame(): 结束游戏
- restartGame(): 重新开始游戏
- handleStateTransition(oldState, newState): 处理状态转换

### UIStateRenderer
职责: 根据游戏状态渲染对应的UI界面
- renderState(state): 渲染状态对应界面
- showPauseOverlay(): 显示暂停遮罩
- showGameOverScreen(): 显示游戏结束界面
- updateButtonStates(state): 更新按钮状态

### InputHandler
职责: 处理用户输入，根据当前状态执行相应操作
- handleKeyPress(key, currentState): 处理按键输入
- enableInput(): 启用输入
- disableInput(): 禁用输入
- bindStateSpecificControls(state): 绑定状态特定控制

### GameLoop
职责: 管理游戏主循环，根据状态控制循环的启停
- start(): 启动游戏循环
- pause(): 暂停游戏循环
- resume(): 恢复游戏循环
- stop(): 停止游戏循环
- setUpdateCallback(callback): 设置更新回调

### PersistenceManager
职责: 管理游戏状态的持久化存储
- saveGameState(state): 保存游戏状态
- loadGameState(): 加载游戏状态
- clearSavedState(): 清除保存的状态
- saveSettings(settings): 保存游戏设置

## 数据流
用户操作 -> InputHandler -> GameController -> GameStateManager -> 状态变化通知 -> UIStateRenderer/GameLoop -> Canvas渲染/循环控制。状态变化时触发PersistenceManager保存数据，游戏启动时从LocalStorage恢复状态。

## 风险点
- 状态转换逻辑复杂，可能出现非法状态转换
- 暂停恢复时游戏数据同步问题
- LocalStorage容量限制和数据损坏风险
- 多个异步操作可能导致状态不一致

## 关键决策
- 采用状态机模式确保状态转换的安全性和可预测性
- 使用观察者模式实现状态变化的响应式更新
- 将状态管理与业务逻辑分离，提高代码可维护性
- 使用requestAnimationFrame确保渲染与状态同步
- 实现状态持久化支持游戏中断恢复功能
