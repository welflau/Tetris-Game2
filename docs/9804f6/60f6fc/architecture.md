# 架构设计 - 开发碰撞检测系统

## 架构模式
模块化架构（Module Pattern）

## 技术栈

- **language**: JavaScript ES6+
- **framework**: HTML5 Canvas
- **database**: 无（客户端游戏）
- **others**: Canvas 2D API, requestAnimationFrame, 事件监听器

## 模块设计

### CollisionDetector
职责: 核心碰撞检测逻辑，提供边界检测、方块间碰撞检测和位置验证功能
- checkBoundaryCollision(piece, x, y, rotation)
- checkPieceCollision(piece, x, y, rotation, gameBoard)
- isValidPosition(piece, x, y, rotation, gameBoard)
- canMoveTo(piece, newX, newY, rotation, gameBoard)
- canRotate(piece, x, y, newRotation, gameBoard)

### GameBoard
职责: 游戏板状态管理，维护10x20网格数据和已放置方块信息
- getCell(x, y)
- setCell(x, y, value)
- isOccupied(x, y)
- getBoard()
- clearBoard()
- placePiece(piece, x, y, rotation)

### Piece
职责: 方块数据结构和形状定义，包含7种俄罗斯方块类型的坐标数据
- getShape(rotation)
- getWidth(rotation)
- getHeight(rotation)
- getBlocks(rotation)
- getType()
- clone()

### MovementController
职责: 方块移动控制器，处理移动、旋转请求并调用碰撞检测
- moveLeft()
- moveRight()
- moveDown()
- rotate()
- drop()
- canPerformAction(action)

### GameConstants
职责: 游戏常量定义，包含游戏板尺寸、方块类型等配置
- BOARD_WIDTH
- BOARD_HEIGHT
- TETROMINOS
- EMPTY_CELL
- COLLISION_TYPES

## 数据流
用户输入 → MovementController → CollisionDetector → GameBoard状态查询 → Piece形状数据获取 → 碰撞检测计算 → 返回检测结果 → MovementController执行或拒绝动作 → 更新游戏状态

## 风险点
- 旋转碰撞检测的边界情况处理复杂
- 高频率碰撞检测可能影响游戏性能
- 不同方块形状的旋转中心点计算容易出错
- 边界检测与方块间碰撞检测的优先级处理

## 关键决策
- 采用基于坐标的碰撞检测算法，通过遍历方块的每个单元格进行检测
- 使用二维数组表示游戏板状态，0表示空位，非0表示已占用
- 实现分层检测策略：先检测边界碰撞，再检测方块间碰撞
- 为每种方块类型预定义4个旋转状态的坐标数据，避免实时计算
- 使用缓存机制优化频繁的碰撞检测调用
- 采用防抖机制处理快速连续的移动操作
