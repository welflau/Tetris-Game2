# 架构设计 - 游戏状态管理与暂停功能

## 架构模式
状态机模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript

## 模块设计

### GameStateManager
职责: 管理游戏状态转换（运行、暂停、游戏结束、重新开始）
- pause()
- resume()
- restart()
- getCurrentState()
- setState(state)
- onStateChange(callback)

### PauseOverlay
职责: 暂停时的UI覆盖层，显示暂停菜单和操作选项
- show()
- hide()
- renderPauseMenu()
- bindEvents()

### GameControlPanel
职责: 游戏控制面板，包含暂停、重新开始等按钮
- render()
- updateButtonStates()
- bindControlEvents()

### StateTransitionHandler
职责: 处理状态转换时的逻辑，如保存游戏数据、停止动画等
- handlePause()
- handleResume()
- handleRestart()
- saveGameState()
- restoreGameState()

## 数据流
用户操作触发GameStateManager状态变更 -> StateTransitionHandler处理状态转换逻辑 -> 更新UI显示（PauseOverlay/GameControlPanel） -> 保存/恢复游戏数据到LocalStorage -> 通知游戏引擎暂停/继续渲染循环

## 关键决策
- 采用状态机模式管理游戏状态，确保状态转换的一致性和可预测性
- 使用覆盖层模式实现暂停界面，不影响游戏画布的渲染状态
- 集成LocalStorage保存暂停时的游戏状态，支持页面刷新后恢复
- 通过事件系统与现有游戏引擎解耦，避免修改核心游戏逻辑
- 设计响应式暂停菜单，适配不同屏幕尺寸
