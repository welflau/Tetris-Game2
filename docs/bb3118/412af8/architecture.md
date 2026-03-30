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
- setState(newState): 设置游戏状态
- getState(): 获取当前状态
- canTransition(fromState, toState): 验证状态转换
- onStateChange(callback): 注册状态变化监听器

### GameStates
职责: 定义所有游戏状态常量和状态行为
- MENU: 主菜单状态
- PLAYING: 游戏进行状态
- PAUSED: 暂停状态
- GAME_OVER: 游戏结束状态
- LOADING: 加载状态

### StateTransitionController
职责: 控制状态转换逻辑和转换动画
- startGame(): 开始游戏
- pauseGame(): 暂停游戏
- resumeGame(): 继续游戏
- endGame(): 结束游戏
- restartGame(): 重新开始

### GameDataManager
职责: 管理游戏数据的持久化和恢复
- saveGameState(gameData): 保存游戏状态
- loadGameState(): 加载游戏状态
- clearGameData(): 清除游戏数据
- hasValidSave(): 检查是否有有效存档

### UIStateController
职责: 根据游戏状态更新UI界面显示
- updateUI(state): 更新界面状态
- showPauseMenu(): 显示暂停菜单
- showGameOverScreen(): 显示游戏结束界面
- hideAllMenus(): 隐藏所有菜单

### InputStateHandler
职责: 根据游戏状态处理不同的输入响应
- handleInput(keyCode, state): 处理按键输入
- enableGameControls(): 启用游戏控制
- disableGameControls(): 禁用游戏控制
- enableMenuControls(): 启用菜单控制

## 数据流
用户操作 -> InputStateHandler -> StateTransitionController -> GameStateManager -> 状态变更通知 -> UIStateController/GameEngine -> 界面更新/游戏逻辑响应。同时GameDataManager负责在关键状态转换时进行数据持久化。

## 风险点
- 状态转换逻辑复杂，可能出现状态不一致
- 暂停恢复功能可能影响游戏计时准确性
- LocalStorage数据损坏导致游戏状态丢失
- 多个异步操作可能导致状态竞争条件

## 关键决策
- 采用状态机模式确保状态转换的安全性和可预测性
- 使用观察者模式解耦状态变化和UI更新
- 实现状态转换验证机制防止非法状态切换
- 使用LocalStorage进行游戏状态持久化
- 设计状态恢复机制支持游戏中断后继续
- 实现防抖机制避免快速按键导致的状态混乱
