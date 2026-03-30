# 架构设计 - 游戏逻辑核心系统开发

## 架构模式
模块化组件架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + HTML5 Canvas

## 模块设计

### GameLogic
职责: 核心游戏逻辑控制器，管理游戏状态、方块移动、下落和碰撞检测
- init(gameBoard, tetrominoSystem)
- update(deltaTime)
- moveBlock(direction)
- rotateBlock()
- dropBlock()
- checkCollision(block, x, y)
- lockBlock()
- getGameState()

### MovementController
职责: 处理方块移动逻辑，包括左右移动、旋转和下落控制
- moveLeft()
- moveRight()
- moveDown()
- rotate()
- softDrop()
- hardDrop()
- isValidMove(block, x, y, rotation)

### CollisionDetector
职责: 碰撞检测系统，检测方块与边界、其他方块的碰撞
- checkBoundaryCollision(block, x, y)
- checkBlockCollision(block, x, y)
- isPositionValid(x, y, shape)
- getCollisionType(block, x, y)

### FallSystem
职责: 方块自动下落系统，管理下落速度和时间控制
- startFall()
- stopFall()
- updateFallSpeed(level)
- resetFallTimer()
- shouldFall()

### GameStateManager
职责: 游戏状态管理，包括运行、暂停、游戏结束等状态
- setState(state)
- getState()
- pause()
- resume()
- gameOver()
- restart()

## 数据流
用户输入 -> MovementController -> CollisionDetector验证 -> GameLogic更新方块位置 -> FallSystem控制自动下落 -> GameStateManager管理游戏状态 -> 通知渲染系统更新显示

## 关键决策
- 采用事件驱动架构，各模块通过事件通信，降低耦合度
- 使用requestAnimationFrame实现平滑的游戏循环和动画效果
- 碰撞检测采用基于网格的算法，提高检测效率
- 方块移动使用缓存验证机制，避免重复计算
- 游戏状态使用状态机模式管理，确保状态转换的正确性
- 集成现有的Canvas渲染系统和Tetromino方块系统，保持架构一致性
