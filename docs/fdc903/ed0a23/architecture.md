# 架构设计 - 实现方块类型和旋转系统

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: 原生JavaScript或轻量级Canvas框架
- **database**: LocalStorage（游戏状态持久化）
- **others**: Canvas API, RAF（RequestAnimationFrame）, Event System

## 模块设计

### BlockType枚举类
职责: 定义七种方块类型常量和基础属性
- getBlockTypes()
- getBlockColor(type)
- getBlockShape(type)

### Shape数据类
职责: 存储方块形状的二维数组表示和旋转状态
- getMatrix()
- rotate()
- getRotationStates()
- clone()

### Block核心类
职责: 管理单个方块实例，包含位置、类型、旋转状态
- move(dx, dy)
- rotate(direction)
- getPosition()
- getShape()
- setRotation(state)

### RotationSystem旋转系统
职责: 处理方块旋转逻辑，包括SRS旋转规则和踢墙检测
- canRotate(block, grid)
- performRotation(block, direction)
- getKickOffsets(type, rotation)

### BlockFactory工厂类
职责: 负责创建和初始化不同类型的方块实例
- createBlock(type)
- getRandomBlock()
- getNextBlocks(count)

### ShapeDefinitions配置类
职责: 存储所有方块类型的形状定义和旋转状态数据
- getShapeData(type)
- getAllShapes()
- validateShape(matrix)

## 数据流
BlockFactory创建Block实例 -> Block包含Shape数据 -> RotationSystem处理旋转请求 -> 通过碰撞检测验证 -> 更新Block状态 -> 渲染系统获取最新形状数据进行绘制

## 风险点
- 旋转踢墙逻辑复杂，需要精确实现SRS标准
- 方块形状数据定义错误可能导致显示异常
- 旋转性能优化，避免频繁的数组操作
- 边界情况处理，如靠近边界时的旋转限制

## 关键决策
- 采用二维数组表示方块形状，便于碰撞检测和渲染
- 实现标准SRS旋转系统，确保游戏体验符合经典俄罗斯方块
- 使用工厂模式创建方块，便于扩展新的方块类型
- 分离形状数据和逻辑，提高代码可维护性
- 预计算所有旋转状态，避免运行时计算开销
