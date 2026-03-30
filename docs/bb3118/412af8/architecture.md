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
- setState(state): void - 设置游戏状态
- getState(): GameState - 获取当前状态
- canTransition(fromState, toState): boolean - 检查状态转换合法性
- subscribe(callback): void - 订阅状态变更事件
- unsubscribe(callback): void - 取消订阅

### GameState
职责: 定义游戏状态枚举和状态数据结构
- MENU: string - 菜单状态
- PLAYING: string - 游戏进行状态
- PAUSED: string - 暂停状态
- GAME_OVER: string - 游戏结束状态
- LOADING: string - 加载状态

### StateTransitionController
职责: 控制状态转换逻辑，验证转换条件，执行转换动作
- startGame(): void - 开始游戏
- pauseGame(): void - 暂停游戏
- resumeGame(): void - 继续游戏
- endGame(): void - 结束游戏
- restartGame(): void - 重新开始游戏
- backToMenu(): void - 返回菜单

### StateRenderer
职责: 根据当前状态渲染对应的UI界面和游戏画面
- renderState(state, context): void - 渲染状态对应界面
- showPauseOverlay(): void - 显示暂停遮罩
- showGameOverScreen(): void - 显示游戏结束界面
- showMenu(): void - 显示主菜单
- hideOverlays(): void - 隐藏所有遮罩

### StateEventHandler
职责: 处理不同状态下的用户输入和系统事件
- handleKeyInput(key, state): void - 处理键盘输入
- handleMenuClick(action): void - 处理菜单点击
- handlePauseToggle(): void - 处理暂停切换
- handleGameOver(): void - 处理游戏结束事件

### GameDataPersistence
职责: 保存和恢复游戏状态数据，管理本地存储
- saveGameState(stateData): void - 保存游戏状态
- loadGameState(): Object - 加载游戏状态
- clearSavedState(): void - 清除保存的状态
- hasValidSavedState(): boolean - 检查是否有有效保存状态

## 数据流
用户操作 -> StateEventHandler -> StateTransitionController -> GameStateManager -> 状态变更通知 -> StateRenderer + GameEngine，同时GameDataPersistence负责状态数据的持久化存储和恢复

## 风险点
- 状态转换逻辑复杂，可能出现非法状态转换
- 暂停状态下的数据一致性问题
- LocalStorage容量限制和数据损坏风险
- 多个状态监听器可能导致内存泄漏

## 关键决策
- 采用状态机模式确保状态转换的安全性和可预测性
- 使用观察者模式解耦状态变更和UI更新
- 将状态渲染独立成模块，便于不同状态下的UI管理
- 使用LocalStorage进行状态持久化，支持游戏中断后恢复
- 实现状态转换的权限控制，防止非法状态切换
