# 架构设计 - 实现碰撞检测系统

## 架构模式
MVC + 策略模式

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: 原生Canvas/WebGL或React
- **database**: LocalStorage（游戏状态持久化）
- **others**: Canvas 2D API, requestAnimationFrame, 事件监听器

## 模块设计

### CollisionDetector
职责: 核心碰撞检测逻辑，检测方块与边界、已放置方块的碰撞
- checkCollision(block, grid, offsetX, offsetY): boolean
- canMove(block, direction, grid): boolean
- canRotate(block, rotationState, grid): boolean
- isValidPosition(block, x, y, grid): boolean

### BoundaryChecker
职责: 检测方块是否超出游戏边界（左右边界、底部边界）
- checkLeftBoundary(block, x): boolean
- checkRightBoundary(block, x, gridWidth): boolean
- checkBottomBoundary(block, y, gridHeight): boolean

### BlockCollisionChecker
职责: 检测方块与已放置方块的碰撞
- checkBlockCollision(block, grid, x, y): boolean
- getOccupiedCells(block, x, y): Array<{x, y}>
- isGridCellOccupied(grid, x, y): boolean

### RotationValidator
职责: 验证方块旋转后的位置是否合法，实现旋转碰撞检测
- validateRotation(block, newRotation, grid): boolean
- getRotationOffset(block, currentRotation, newRotation): {x, y}
- tryWallKick(block, rotation, grid): {x, y} | null

### MovementValidator
职责: 验证方块移动的合法性，包括左右移动和下落
- validateMove(block, direction, grid): boolean
- getNextPosition(block, direction): {x, y}
- canMoveDown(block, grid): boolean

## 数据流
Game类调用CollisionDetector进行碰撞检测 -> CollisionDetector根据检测类型分发给BoundaryChecker或BlockCollisionChecker -> 各检测器返回布尔值结果 -> CollisionDetector汇总结果返回给Game类 -> Game类根据结果决定是否允许移动/旋转操作

## 风险点
- 复杂旋转状态下的碰撞检测可能出现边界情况
- Wall Kick机制实现复杂度较高
- 性能优化：频繁的碰撞检测可能影响60fps目标
- 不同方块形状的旋转中心点计算复杂

## 关键决策
- 采用策略模式分离不同类型的碰撞检测逻辑，提高代码可维护性
- 使用坐标系统进行精确的位置计算，避免像素级碰撞检测
- 实现Wall Kick机制以提供更好的游戏体验
- 预计算方块的所有旋转状态，避免实时计算提高性能
- 使用位运算优化网格占用状态检查
