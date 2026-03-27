# 架构设计 - 实现方块移动和下落逻辑

## 架构模式
MVC + 状态机模式

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: 原生 Canvas API 或 React
- **database**: LocalStorage（游戏状态持久化）
- **others**: requestAnimationFrame, 事件监听器, 定时器

## 模块设计

### MovementController
职责: 处理方块移动逻辑，包括左右移动、快速下落、自动下落的控制
- moveLeft()
- moveRight()
- moveDown()
- drop()
- startAutoFall()
- stopAutoFall()

### CollisionDetector
职责: 检测方块与网格边界、已放置方块的碰撞，验证移动有效性
- checkCollision(block, grid, newX, newY)
- isValidPosition()
- canMoveLeft()
- canMoveRight()
- canMoveDown()

### Block
职责: 方块实体类，维护方块位置、形状、旋转状态
- getPosition()
- setPosition(x, y)
- getShape()
- move(dx, dy)
- isActive()

### Grid
职责: 游戏网格管理，维护已放置方块状态
- getCellState(x, y)
- setCellState(x, y, state)
- isRowFull(row)
- clearRow(row)

### GameTimer
职责: 管理游戏时间循环，控制自动下落间隔和帧率
- start()
- stop()
- setFallSpeed(speed)
- tick()

### InputHandler
职责: 处理键盘输入事件，将输入转换为游戏动作
- bindKeyEvents()
- handleKeyDown(event)
- handleKeyUp(event)

## 数据流
用户按键 -> InputHandler 捕获事件 -> MovementController 处理移动请求 -> CollisionDetector 验证移动有效性 -> Block 更新位置 -> Grid 更新状态 -> 渲染引擎重绘。GameTimer 定期触发自动下落，遵循相同流程

## 风险点
- 高频率移动操作可能导致性能问题
- 碰撞检测算法复杂度影响流畅性
- 键盘事件重复触发导致移动过快
- 自动下落与手动操作的时间冲突

## 关键决策
- 使用requestAnimationFrame确保60fps渲染
- 实现键盘事件防抖机制避免过快移动
- 采用预测性碰撞检测提高性能
- 使用状态机管理方块移动状态
- 分离移动逻辑和渲染逻辑实现解耦
