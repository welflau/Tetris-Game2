# 俄罗斯方块游戏完整设计文档

## 1. 项目概述

### 1.1 项目简介
俄罗斯方块（Tetris）是一款经典的益智类游戏，玩家需要控制不断下落的四方格组成的几何图形（称为"俄罗斯方块"），通过旋转和移动使其在游戏区域底部排列成完整的水平线来消除。

### 1.2 项目目标
- 实现一个完整功能的俄罗斯方块游戏
- 提供流畅的游戏体验和直观的用户界面
- 支持多种游戏模式和难度设置
- 实现排行榜和成就系统
- 确保跨平台兼容性

### 1.3 技术栈
- **前端**: HTML5 Canvas, CSS3, JavaScript (ES6+)
- **后端**: Python Flask (可选，用于排行榜)
- **数据库**: SQLite/LocalStorage
- **构建工具**: Webpack
- **测试**: Jest

## 2. 游戏规则与机制

### 2.1 基本规则
1. 游戏区域为 10×20 的网格
2. 七种不同形状的方块（Tetromino）从顶部随机出现
3. 方块自动向下移动，玩家可以控制移动和旋转
4. 当一行完全填满时，该行消除并获得分数
5. 当方块堆积到顶部时，游戏结束

### 2.2 方块类型（Tetromino）
| 名称 | 形状 | 颜色 | 特点 |
|------|------|------|------|
| I-Block | ████ | 青色 | 直线形，可消除4行 |
| O-Block | ██<br>██ | 黄色 | 正方形，无旋转变化 |
| T-Block | █<br>███ | 紫色 | T字形，4种旋转状态 |
| S-Block | ██<br>██ | 绿色 | S字形，2种旋转状态 |
| Z-Block | ██<br>██ | 红色 | Z字形，2种旋转状态 |
| J-Block | █<br>███ | 蓝色 | J字形，4种旋转状态 |
| L-Block | █<br>███ | 橙色 | L字形，4种旋转状态 |

### 2.3 控制方式
- **A/左箭头**: 向左移动
- **D/右箭头**: 向右移动
- **S/下箭头**: 快速下降
- **W/上箭头**: 旋转方块
- **空格**: 瞬间下降到底部
- **P**: 暂停/继续游戏

### 2.4 计分系统
- **单行消除**: 100 × 等级
- **双行消除**: 300 × 等级
- **三行消除**: 500 × 等级
- **四行消除（Tetris）**: 800 × 等级
- **软降**: 每格 1 分
- **硬降**: 每格 2 分

## 3. 系统架构设计

### 3.1 整体架构
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   游戏引擎层     │    │   渲染层        │    │   用户界面层     │
│  Game Engine    │    │  Renderer       │    │      UI         │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ • 游戏逻辑      │    │ • Canvas渲染    │    │ • 主菜单        │
│ • 状态管理      │    │ • 动画效果      │    │ • 游戏界面      │
│ • 碰撞检测      │    │ • 粒子系统      │    │ • 设置页面      │
│ • 消行算法      │    │ • 音效管理      │    │ • 排行榜        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
           │                       │                       │
           └───────────────────────┼───────────────────────┘
                                   │
                    ┌─────────────────┐
                    │   数据层        │
                    │  Data Layer     │
                    ├─────────────────┤
                    │ • 游戏状态      │
                    │ • 用户数据      │
                    │ • 配置信息      │
                    │ • 排行榜数据    │
                    └─────────────────┘
```

## 4. 核心算法实现

### 4.1 碰撞检测算法
```javascript
function checkCollision(board, piece, x, y) {
    const shape = piece.getRotatedShape();
    for (let row = 0; row < shape.length; row++) {
        for (let col = 0; col < shape[row].length; col++) {
            if (shape[row][col]) {
                const newX = x + col;
                const newY = y + row;
                
                // 边界检测
                if (newX < 0 || newX >= board.width || newY >= board.height) {
                    return true;
                }
                
                // 方块碰撞检测
                if (newY >= 0 && board.grid[newY][newX]) {
                    return true;
                }
            }
        }
    }
    return false;
}
```

### 4.2 消行算法
```javascript
function clearLines(board) {
    let linesCleared = 0;
    let linesToClear = [];
    
    // 找出所有满行
    for (let y = board.height - 1; y >= 0; y--) {
        if (board.grid[y].every(cell => cell !== 0)) {
            linesToClear.push(y);
        }
    }
    
    // 清除满行并下移
    linesToClear.forEach(lineIndex => {
        board.grid.splice(lineIndex, 1);
        board.grid.unshift(Array(board.width).fill(0));
        linesCleared++;
    });
    
    return linesCleared;
}
```

### 4.3 方块旋转算法
```javascript
function rotateMatrix(matrix) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    const rotated = Array(cols).fill().map(() => Array(rows).fill(0));
    
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            rotated[col][rows - 1 - row] = matrix[row][col];
        }
    }
    
    return rotated;
}
```

## 5. 开发计划

### 5.1 开发阶段
1. **第一阶段**: 核心游戏逻辑（2周）
   - 游戏板和方块系统
   - 碰撞检测和消行逻辑
   - 基本的渲染系统

2. **第二阶段**: 用户界面（1周）
   - 游戏界面设计
   - 菜单系统
   - 响应式布局

3. **第三阶段**: 增强功能（1周）
   - 音效系统
   - 动画效果
   - 本地存储

4. **第四阶段**: 测试优化（1周）
   - 性能优化
   - 兼容性测试
   - 用户体验优化

### 5.2 技术难点
- Canvas 性能优化
- 精确的碰撞检测
- 流畅的动画效果
- 跨浏览器兼容性

## 6. 总结

这个俄罗斯方块游戏设计文档提供了完整的开发指南，包括游戏机制、技术架构、核心算法和开发计划。通过模块化的设计和现代 Web 技术的应用，可以实现一个功能完整、性能优良的俄罗斯方块游戏。

---
*文档创建时间: 2026-03-30*
*版本: 1.0*