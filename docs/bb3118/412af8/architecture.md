# 架构设计 - 游戏状态管理系统

## 架构模式
状态机模式 + 观察者模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript
- **database**: LocalStorage
- **others**: HTML5 Canvas, CSS3, Web Audio API

## 模块设计

### GameStateManager
职责: 管理游戏状态转换，维护状态机，处理状态变更事件
- setState(newState): 设置游戏状态
- getCurrentState(): 获取当前状态
- canTransitionTo(targetState): 检查状态转换是否合法
- addStateListener(callback): 添加状态变更监听器
- removeStateListener(callback): 移除状态变更监听器

### GameState
职责: 定义游戏状态枚举和状态转换规则
- MENU: 主菜单状态
- PLAYING: 游戏进行状态
- PAUSED: 游戏暂停状态
- GAME_OVER: 游戏结束状态
- LOADING: 游戏加载状态

### StateTransitionController
职责: 控制状态转换逻辑，验证转换合法性，触发相应动作
- startGame(): 开始游戏
- pauseGame(): 暂停游戏
- resumeGame(): 继续游戏
- endGame(): 结束游戏
- restartGame(): 重新开始游戏
- returnToMenu(): 返回主菜单

### GameDataPersistence
职责: 处理游戏数据的持久化存储，包括进度保存和恢复
- saveGameState(gameData): 保存游戏状态
- loadGameState(): 加载游戏状态
- clearSavedState(): 清除保存的状态
- hasSavedGame(): 检查是否有保存的游戏

### UIStateRenderer
职责: 根据游戏状态渲染对应的UI界面和提示信息
- renderMenuUI(): 渲染菜单界面
- renderGameUI(): 渲染游戏界面
- renderPauseOverlay(): 渲染暂停覆盖层
- renderGameOverUI(): 渲染游戏结束界面
- showStateTransition(fromState, toState): 显示状态转换动画

### InputStateHandler
职责: 根据当前游戏状态处理不同的输入事件
- handleMenuInput(event): 处理菜单状态输入
- handleGameInput(event): 处理游戏状态输入
- handlePauseInput(event): 处理暂停状态输入
- handleGameOverInput(event): 处理游戏结束状态输入

## 数据流
用户输入 -> InputStateHandler -> StateTransitionController -> GameStateManager -> 状态变更通知 -> UIStateRenderer + GameDataPersistence，同时GameStateManager通过观察者模式通知所有注册的监听器进行相应的状态处理

## 风险点
- 状态转换逻辑复杂可能导致状态不一致
- 多个组件同时监听状态变更可能产生竞态条件
- LocalStorage数据损坏或丢失导致状态恢复失败
- 状态转换动画与游戏逻辑不同步

## 关键决策
- 采用状态机模式确保状态转换的合法性和一致性
- 使用观察者模式实现松耦合的状态变更通知机制
- 将UI渲染和数据持久化分离，提高模块独立性
- 实现输入处理的状态上下文切换，避免无效操作
- 使用枚举定义状态常量，提高代码可维护性
- 添加状态转换验证机制，防止非法状态切换
