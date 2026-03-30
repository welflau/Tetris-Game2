/**
 * 消行系统和计分系统 - 功能模块
 * 实现满行检测、消除动画、计分规则和等级系统
 */

// 满行检测器
class LineDetector {
    /**
     * 检测游戏区域中的满行
     * @param {Array} gameBoard - 游戏区域二维数组
     * @returns {Array} 满行的索引数组
     */
    detectFullLines(gameBoard) {
        const fullLines = [];
        for (let row = 0; row < gameBoard.length; row++) {
            if (this.isLineFull(gameBoard[row])) {
                fullLines.push(row);
            }
        }
        return fullLines;
    }

    /**
     * 检查单行是否已满
     * @param {Array} lineArray - 行数组
     * @returns {boolean} 是否已满
     */
    isLineFull(lineArray) {
        return lineArray.every(cell => cell !== 0);
    }
}

// 消行动画器
class LineClearAnimator {
    constructor() {
        this.animationDuration = 600; // 动画持续时间
        this.flashCount = 3; // 闪烁次数
        this.isAnimating = false;
        this.completionCallback = null;
    }

    /**
     * 播放消行动画
     * @param {Array} lineIndexes - 要消除的行索引
     * @param {HTMLCanvasElement} canvas - Canvas元素
     * @param {CanvasRenderingContext2D} ctx - Canvas上下文
     * @param {Object} gameConfig - 游戏配置
     */
    playLineClearAnimation(lineIndexes, canvas, ctx, gameConfig) {
        if (this.isAnimating || lineIndexes.length === 0) return;
        
        this.isAnimating = true;
        const { blockSize, gameArea } = gameConfig;
        let flashPhase = 0;
        const flashInterval = this.animationDuration / (this.flashCount * 2);
        
        const animate = () => {
            // 闪烁效果
            const isVisible = Math.floor(flashPhase / flashInterval) % 2 === 0;
            
            // 清除要消除的行
            lineIndexes.forEach(rowIndex => {
                const y = rowIndex * blockSize;
                ctx.fillStyle = isVisible ? 'rgba(255, 255, 255, 0.8)' : 'rgba(255, 255, 0, 0.6)';
                ctx.fillRect(gameArea.x, gameArea.y + y, gameArea.width, blockSize);
            });
            
            flashPhase += 16; // 假设60fps
            
            if (flashPhase < this.animationDuration) {
                requestAnimationFrame(animate);
            } else {
                this.isAnimating = false;
                if (this.completionCallback) {
                    this.completionCallback();
                }
            }
        };
        
        requestAnimationFrame(animate);
    }

    /**
     * 设置动画完成回调
     * @param {Function} callback - 回调函数
     */
    onAnimationComplete(callback) {
        this.completionCallback = callback;
    }

    /**
     * 检查是否正在播放动画
     * @returns {boolean}
     */
    isPlaying() {
        return this.isAnimating;
    }
}

// 分数计算器
class ScoreCalculator {
    constructor() {
        // 经典俄罗斯方块计分规则
        this.scoreTable = {
            1: 100,  // 单行
            2: 300,  // 双行
            3: 500,  // 三行
            4: 800   // 四行（Tetris）
        };
    }

    /**
     * 计算分数
     * @param {number} linesCleared - 消除的行数
     * @param {number} level - 当前等级
     * @returns {number} 获得的分数
     */
    calculateScore(linesCleared, level) {
        if (linesCleared === 0) return 0;
        
        const baseScore = this.scoreTable[linesCleared] || 0;
        const levelMultiplier = level + 1;
        
        return baseScore * levelMultiplier;
    }

    /**
     * 获取分数倍数
     * @param {number} linesCleared - 消除的行数
     * @returns {number} 分数倍数
     */
    getScoreMultiplier(linesCleared) {
        const multipliers = {
            1: 1.0,
            2: 3.0,
            3: 5.0,
            4: 8.0
        };
        return multipliers[linesCleared] || 1.0;
    }

    /**
     * 计算软降分数（快速下降奖励）
     * @param {number} dropDistance - 下降距离
     * @returns {number} 软降分数
     */
    calculateSoftDropScore(dropDistance) {
        return dropDistance; // 每格1分
    }

    /**
     * 计算硬降分数（瞬间下降奖励）
     * @param {number} dropDistance - 下降距离
     * @returns {number} 硬降分数
     */
    calculateHardDropScore(dropDistance) {
        return dropDistance * 2; // 每格2分
    }
}

// 等级管理器
class LevelManager {
    constructor() {
        this.currentLevel = 1;
        this.totalLinesCleared = 0;
        this.linesPerLevel = 10; // 每10行升一级
        this.maxLevel = 20;
        this.baseDropSpeed = 1000; // 基础下落速度（毫秒）
        this.speedMultiplier = 0.8; // 每级速度倍数
    }

    /**
     * 更新等级
     * @param {number} newLinesCleared - 新消除的行数
     * @returns {boolean} 是否升级了
     */
    updateLevel(newLinesCleared) {
        const oldLevel = this.currentLevel;
        this.totalLinesCleared += newLinesCleared;
        
        const newLevel = Math.min(
            Math.floor(this.totalLinesCleared / this.linesPerLevel) + 1,
            this.maxLevel
        );
        
        this.currentLevel = newLevel;
        return newLevel > oldLevel;
    }

    /**
     * 获取当前等级的下落速度
     * @param {number} level - 等级（可选，默认使用当前等级）
     * @returns {number} 下落间隔时间（毫秒）
     */
    getDropSpeed(level = this.currentLevel) {
        return Math.max(
            this.baseDropSpeed * Math.pow(this.speedMultiplier, level - 1),
            50 // 最快速度限制
        );
    }

    /**
     * 检查是否应该升级
     * @returns {boolean}
     */
    checkLevelUp() {
        const expectedLevel = Math.floor(this.totalLinesCleared / this.linesPerLevel) + 1;
        return expectedLevel > this.currentLevel && this.currentLevel < this.maxLevel;
    }

    /**
     * 获取升级所需的剩余行数
     * @returns {number}
     */
    getLinesUntilNextLevel() {
        if (this.currentLevel >= this.maxLevel) return 0;
        const nextLevelLines = this.currentLevel * this.linesPerLevel;
        return nextLevelLines - this.totalLinesCleared;
    }

    /**
     * 重置等级管理器
     */
    reset() {
        this.currentLevel = 1;
        this.totalLinesCleared = 0;
    }
}

// 游戏统计数据
class GameStats {
    constructor() {
        this.score = 0;
        this.level = 1;
        this.lines = 0;
        this.totalLines = 0;
        this.time = 0;
        this.startTime = null;
        this.gameStarted = false;
        
        // 详细统计
        this.singleLines = 0;
        this.doubleLines = 0;
        this.tripleLines = 0;
        this.tetrisLines = 0;
        this.totalPieces = 0;
        
        this.loadFromStorage();
    }

    /**
     * 更新统计数据
     * @param {number} score - 分数增量
     * @param {number} lines - 消行数
     * @param {number} level - 当前等级
     */
    updateStats(score, lines, level) {
        this.score += score;
        this.lines += lines;
        this.totalLines += lines;
        this.level = level;
        
        // 更新详细统计
        switch(lines) {
            case 1: this.singleLines++; break;
            case 2: this.doubleLines++; break;
            case 3: this.tripleLines++; break;
            case 4: this.tetrisLines++; break;
        }
        
        this.updateTime();
        this.saveToStorage();
    }

    /**
     * 增加方块计数
     */
    incrementPieces() {
        this.totalPieces++;
        this.saveToStorage();
    }

    /**
     * 开始游戏计时
     */
    startGame() {
        this.startTime = Date.now();
        this.gameStarted = true;
    }

    /**
     * 更新游戏时间
     */
    updateTime() {
        if (this.gameStarted && this.startTime) {
            this.time = Date.now() - this.startTime;
        }
    }

    /**
     * 格式化时间显示
     * @returns {string} 格式化的时间字符串
     */
    getFormattedTime() {
        const seconds = Math.floor(this.time / 1000);
        const minutes = Math.floor(seconds / 60);
        const hours = Math.floor(minutes / 60);
        
        if (hours > 0) {
            return `${hours}:${(minutes % 60).toString().padStart(2, '0')}:${(seconds % 60).toString().padStart(2, '0')}`;
        } else {
            return `${minutes}:${(seconds % 60).toString().padStart(2, '0')}`;
        }
    }

    /**
     * 计算每分钟行数 (LPM)
     * @returns {number}
     */
    getLinesPerMinute() {
        if (this.time === 0) return 0;
        return Math.round((this.totalLines * 60000) / this.time);
    }

    /**
     * 计算每分钟方块数 (PPM)
     * @returns {number}
     */
    getPiecesPerMinute() {
        if (this.time === 0) return 0;
        return Math.round((this.totalPieces * 60000) / this.time);
    }

    /**
     * 保存到本地存储
     */
    saveToStorage() {
        const data = {
            score: this.score,
            level: this.level,
            lines: this.lines,
            totalLines: this.totalLines,
            time: this.time,
            singleLines: this.singleLines,
            doubleLines: this.doubleLines,
            tripleLines: this.tripleLines,
            tetrisLines: this.tetrisLines,
            totalPieces: this.totalPieces,
            lastUpdated: Date.now()
        };
        
        try {
            localStorage.setItem('tetris_current_stats', JSON.stringify(data));
        } catch (e) {
            console.warn('无法保存游戏统计数据到本地存储:', e);
        }
    }

    /**
     * 从本地存储加载
     */
    loadFromStorage() {
        try {
            const data = localStorage.getItem('tetris_current_stats');
            if (data) {
                const parsed = JSON.parse(data);
                Object.assign(this, parsed);
            }
        } catch (e) {
            console.warn('无法从本地存储加载游戏统计数据:', e);
        }
    }

    /**
     * 重置统计数据
     */
    reset() {
        this.score = 0;
        this.level = 1;
        this.lines = 0;
        this.totalLines = 0;
        this.time = 0;
        this.startTime = null;
        this.gameStarted = false;
        this.singleLines = 0;
        this.doubleLines = 0;
        this.tripleLines = 0;
        this.tetrisLines = 0;
        this.totalPieces = 0;
        
        this.saveToStorage();
    }

    /**
     * 获取统计摘要
     * @returns {Object} 统计摘要对象
     */
    getSummary() {
        return {
            score: this.score,
            level: this.level,
            lines: this.totalLines,
            time: this.getFormattedTime(),
            lpm: this.getLinesPerMinute(),
            ppm: this.getPiecesPerMinute(),
            efficiency: {
                single: this.singleLines,
                double: this.doubleLines,
                triple: this.tripleLines,
                tetris: this.tetrisLines
            }
        };
    }
}

// 消行控制器 - 协调整个消行流程
class LineClearController {
    constructor() {
        this.lineDetector = new LineDetector();
        this.animator = new LineClearAnimator();
        this.scoreCalculator = new ScoreCalculator();
        this.levelManager = new LevelManager();
        this.gameStats = new GameStats();
        
        this.observers = [];
        this.isProcessing = false;
    }

    /**
     * 添加观察者
     * @param {Function} observer - 观察者函数
     */
    addObserver(observer) {
        this.observers.push(observer);
    }

    /**
     * 通知观察者
     * @param {string} event - 事件类型
     * @param {Object} data - 事件数据
     */
    notifyObservers(event, data) {
        this.observers.forEach(observer => {
            try {
                observer(event, data);
            } catch (e) {
                console.error('观察者通知错误:', e);
            }
        });
    }

    /**
     * 处理消行流程
     * @param {Array} gameBoard - 游戏区域
     * @param {HTMLCanvasElement} canvas - Canvas元素
     * @param {CanvasRenderingContext2D} ctx - Canvas上下文
     * @param {Object} gameConfig - 游戏配置
     * @returns {Promise} 处理完成的Promise
     */
    async processLineClear(gameBoard, canvas, ctx, gameConfig) {
        if (this.isProcessing) return;
        
        const fullLines = this.lineDetector.detectFullLines(gameBoard);
        if (fullLines.length === 0) return;
        
        this.isProcessing = true;
        
        try {
            // 播放消行动画
            await this.playLineClearAnimation(fullLines, canvas, ctx, gameConfig);
            
            // 移除满行
            this.removeLines(gameBoard, fullLines);
            
            // 计算分数
            const score = this.scoreCalculator.calculateScore(fullLines.length, this.levelManager.currentLevel);
            
            // 更新等级
            const leveledUp = this.levelManager.updateLevel(fullLines.length);
            
            // 更新统计
            this.gameStats.updateStats(score, fullLines.length, this.levelManager.currentLevel);
            
            // 通知观察者
            this.notifyObservers('linesCleared', {
                lines: fullLines.length,
                score: score,
                level: this.levelManager.currentLevel,
                leveledUp: leveledUp,
                stats: this.gameStats.getSummary()
            });
            
            if (leveledUp) {
                this.notifyObservers('levelUp', {
                    newLevel: this.levelManager.currentLevel,
                    newSpeed: this.levelManager.getDropSpeed()
                });
            }
            
        } finally {
            this.isProcessing = false;
        }
    }

    /**
     * 播放消行动画（Promise版本）
     * @param {Array} lineIndexes - 行索引
     * @param {HTMLCanvasElement} canvas - Canvas元素
     * @param {CanvasRenderingContext2D} ctx - Canvas上下文
     * @param {Object} gameConfig - 游戏配置
     * @returns {Promise}
     */
    playLineClearAnimation(lineIndexes, canvas, ctx, gameConfig) {
        return new Promise((resolve) => {
            this.animator.onAnimationComplete(resolve);
            this.animator.playLineClearAnimation(lineIndexes, canvas, ctx, gameConfig);
        });
    }

    /**
     * 移除满行并下移上方行
     * @param {Array} gameBoard - 游戏区域
     * @param {Array} lineIndexes - 要移除的行索引
     */
    removeLines(gameBoard, lineIndexes) {
        // 从下往上移除行，避免索引变化问题
        const sortedIndexes = [...lineIndexes].sort((a, b) => b - a);
        
        sortedIndexes.forEach(rowIndex => {
            // 移除该行
            gameBoard.splice(rowIndex, 1);
            // 在顶部添加新的空行
            gameBoard.unshift(new Array(gameBoard[0]?.length || 10).fill(0));
        });
    }

    /**
     * 消行完成回调
     */
    onLineClearComplete() {
        this.notifyObservers('lineClearComplete', {
            stats: this.gameStats.getSummary()
        });
    }

    /**
     * 获取当前游戏状态
     * @returns {Object}
     */
    getGameState() {
        return {
            score: this.gameStats.score,
            level: this.levelManager.currentLevel,
            lines: this.gameStats.totalLines,
            dropSpeed: this.levelManager.getDropSpeed(),
            linesUntilNextLevel: this.levelManager.getLinesUntilNextLevel(),
            isProcessing: this.isProcessing
        };
    }

    /**
     * 重置游戏状态
     */
    reset() {
        this.levelManager.reset();
        this.gameStats.reset();
        this.isProcessing = false;
        
        this.notifyObservers('gameReset', {
            stats: this.gameStats.getSummary()
        });
    }

    /**
     * 开始新游戏
     */
    startNewGame() {
        this.reset();
        this.gameStats.startGame();
        
        this.notifyObservers('gameStarted', {
            stats: this.gameStats.getSummary()
        });
    }

    /**
     * 处理软降分数
     * @param {number} distance - 下降距离
     */
    handleSoftDrop(distance) {
        const score = this.scoreCalculator.calculateSoftDropScore(distance);
        this.gameStats.updateStats(score, 0, this.levelManager.currentLevel);
        
        this.notifyObservers('softDrop', {
            score: score,
            distance: distance
        });
    }

    /**
     * 处理硬降分数
     * @param {number} distance - 下降距离
     */
    handleHardDrop(distance) {
        const score = this.scoreCalculator.calculateHardDropScore(distance);
        this.gameStats.updateStats(score, 0, this.levelManager.currentLevel);
        
        this.notifyObservers('hardDrop', {
            score: score,
            distance: distance
        });
    }

    /**
     * 处理方块放置
     */
    handlePiecePlaced() {
        this.gameStats.incrementPieces();
        
        this.notifyObservers('piecePlaced', {
            totalPieces: this.gameStats.totalPieces
        });
    }
}

// 导出所有类
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        LineDetector,
        LineClearAnimator,
        ScoreCalculator,
        LevelManager,
        GameStats,
        LineClearController
    };
} else {
    // 浏览器环境，添加到全局对象
    window.TetrisLineClearSystem = {
        LineDetector,
        LineClearAnimator,
        ScoreCalculator,
        LevelManager,
        GameStats,
        LineClearController
    };
}

console.log('消行系统和计分系统模块已加载');