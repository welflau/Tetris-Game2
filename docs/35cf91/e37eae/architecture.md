# 架构设计 - 设计投影方块视觉方案

## 架构模式
组件化前端架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: Canvas API / WebGL
- **database**: LocalStorage (配置存储)
- **others**: CSS3, HTML5 Canvas, Color.js (颜色处理), Jest (单元测试)

## 模块设计

### GhostPieceRenderer
职责: 负责投影方块的渲染逻辑，包括透明度控制、轮廓线绘制、颜色计算
- drawGhost(piece, position, style)
- setOpacity(value)
- setRenderMode(mode)
- calculateGhostColor(originalColor)

### VisualStyleManager
职责: 管理多种视觉样式方案，提供样式切换和配置功能
- getStyleConfig(styleName)
- switchStyle(styleName)
- registerStyle(config)
- validateStyle(config)

### ContrastDetector
职责: 检测背景对比度，动态调整投影方块的可见性参数
- analyzeBackground(gameBoard)
- calculateOptimalOpacity(background)
- getContrastRatio(color1, color2)

### ConfigurationPanel
职责: 提供用户界面供玩家自定义投影方块样式
- showStyleOptions()
- previewStyle(config)
- saveUserPreference(config)
- resetToDefault()

## 数据流
游戏引擎获取当前方块信息 → VisualStyleManager确定渲染样式 → ContrastDetector分析背景对比度 → GhostPieceRenderer应用样式参数渲染投影方块 → Canvas显示最终效果

## 风险点
- 不同设备屏幕亮度差异可能影响可见性
- 颜色盲用户可能难以区分某些透明度设置
- 高刷新率下透明度渲染可能影响性能
- 移动设备上触摸操作可能遮挡投影方块

## 关键决策
- 采用多层次透明度方案：超透明(0.1)、标准透明(0.3)、轮廓线模式
- 使用HSL颜色空间便于动态调整亮度和饱和度
- 实现自适应对比度算法，根据背景自动调整投影可见性
- 提供用户自定义选项，支持个性化视觉偏好设置
- 采用Canvas离屏渲染优化透明度绘制性能
