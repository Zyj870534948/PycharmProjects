
//gobang 封装实现
(function(){
    //定义变量
    var chess = document.getElementById('chess');  //获取棋盘画布
    var ctx = chess.getContext('2d');  //设置画布渲染
    var logo = new Image(); //创建棋盘背景图像
    var chessBoard = new Array();  //棋盘落子统计，用于存储棋盘格上是否有落子
    var wins = [];  //赢法数组
    var count = 0;  //赢法统计数组
    var myWin = [];  //玩家赢法统计
    var computerWin = [];  //计算机赢法统计
    var me = true; //棋手标记 true为玩家下棋，false为电脑下棋
    var over = false; //判断对局是否结束标记 true为结束，flase为未结束

    var goBang = {
        //入口
        init: function(){
            var _this = this;  //复制this对象
            return (function(){
                //变量初始化
                _this.initializa();
                //图片加载点
                logo.onload = function(){
                    //填充背景图片
                    ctx.drawImage(logo,0,0,450,450);
                    //绘制棋盘线
                    _this.drawChessBoard();
                    // _this.oneStep(7,7,false); //测试oneStep函数
                };

                //落子事件绑定
                //点击棋盘落子
                chess.onclick = function(e){
                    //判断对局是否结束或是否轮到玩家下棋，对局结束或者不是玩家下棋就会跳出循环
                     if(over || me == false){
                         return ;
                     }
                     //获取鼠标点击位置坐标，并转换为落点坐标
                     var x = e.offsetX,
                         y = e.offsetY;
                     var i = Math.floor(x / 30),
                         j = Math.floor(y / 30);
                     //判断当前落点是否已有棋子，如果没有则落子成功
                     if(chessBoard[i][j] == 0){
                         _this.oneStep(i, j, me);  //玩家落子
                         chessBoard[i][j] = 1;   //玩家黑棋落子为1
                         for(var k=0; k<count; k++){
                             if(wins[i][j][k]){
                                 myWin[k]++;
                                 computerWin[k] = 999; //设置成比5大的数都不会加分
                                 if(myWin[k] == 5){
                                     window.alert("You Win !");
                                     over = true;
                                 }
                             }
                         }
                         //判断对局是否未结束，如果未结束将换成计算机下子
                         if(over == false){
                             me = !me;
                             _this.computerAI(); //计算机落子
                         }
                     }
                 };

                 //更改鼠标指针样式
                 chess.onmousemove = function(e){
                     chess.style.cursor = "default";
                     var x = e.offsetX;
                     var y = e.offsetY;
                     for(var i=0; i<15; i++){
                         for(var j=0; j<15; j++){
                             var a = x - (15+i*30);
                             var b = y - (15+j*30);
                             var distance = Math.hypot(a, b);
                             var chessRange = Math.sqrt(25, 2);
                             //在交叉处半径为5的范围内，鼠标变成手指样式
                             if(distance < chessRange){
                                 chess.style.cursor = "pointer";
                             }
                         }
                     }
                 };

             })();
         },

         //变量&初始化&参数设置
         initializa: function(){
             return (function(){
                 //棋盘线条颜色
                 ctx.strokeStyle = "#000000"; //黑色
                 //载入背景图片
                 logo.src = "logo.jpg";
                 //棋盘棋盘落子统计初始化(无落子) chessBoard
                 for (var i=0; i<15; i++) {
                     chessBoard[i] = [];
                     for(var j=0; j<15; j++){
                         chessBoard[i][j] = 0;
                     }
                 }
                 //定义赢法的三维数组 wins
                 for(var i=0; i<15; i++){
                     wins[i] = [];
                     for(var j=0; j<15; j++){
                         wins[i][j] = [];
                     }
                 }
                 //赢法总类统计 共计572种
                 //横线赢法
                 for(var i=0; i<15; i++){
                     for(var j=0; j<11; j++){
                         for(var k=0; k<5; k++){
                             wins[i][j+k][count] = true;
                         }
                         count++;
                     }
                 }
                 //竖线赢法
                 for(var i=0; i<15; i++){
                     for(var j=0; j<11; j++){
                         for(var k=0; k<5; k++){
                             wins[j+k][i][count] = true;
                         }
                         count++;
                     }
                 }
                 //斜线赢法
                 for(var i=0; i<11; i++){
                     for(var j=0; j<11; j++){
                         for(var k=0; k<5; k++){
                             wins[i+k][j+k][count] = true;
                         }
                         count++;
                     }
                 }
                 //反斜线赢法
                 for(var i = 0; i < 11; i++){
                     for(var j= 14; j > 3; j--){
                         for(var k = 0; k < 5; k++){
                             wins[i+k][j-k][count] = true;
                         }
                         count++;
                     }
                 }
                 console.log(count);  //赢法总类输出
                 //赢法统计数组初始化
                 for(var i=0; i<count; i++){
                     myWin[i] = 0;
                     computerWin[i] = 0;
                 }
             })();
         },

         //绘制棋盘
         drawChessBoard: function(){
             return (function(){
                 for(var i=0; i<15; i++){
                     //画棋盘竖线
                     ctx.moveTo(15+i*30, 15);
                     ctx.lineTo(15+i*30, 435);
                     ctx.stroke();
                     //画棋盘横线
                     ctx.moveTo(15, 15+i*30);
                     ctx.lineTo(435, 15+i*30);
                     ctx.stroke();
                 }
             })();
         },

         //绘制黑白棋子
         oneStep: function(i, j, me){
             return (function(){
                 //阴影
                 ctx.shadowOffsetX = 1.5;
                 ctx.shadowOffsetY = 2;
                 ctx.shadowBlur = 3;
                 ctx.shadowColor = '#333';
                 //画圆
                 ctx.beginPath();
                 ctx.arc(15 + i*30, 15 + j*30, 13, 0, 2 * Math.PI);
                 ctx.closePath();
                 //渐变
                 var grd = ctx.createRadialGradient(15 + i*30 + 2, 15 + j*30 - 2, 13, 15 + i*30 + 2, 15 + j*30 - 2, 0);
                 if(me){ //黑棋
                     grd.addColorStop(0, "#0A0A0A");
                     grd.addColorStop(1, "#636766");
                 }
                 else{  //白棋
                     grd.addColorStop(0, "#D1D1D1");
                     grd.addColorStop(1, "#F9F9F9");
                 }
                 ctx.fillStyle = grd;
                 ctx.fill();
             })();
         },

         //计算机下棋
         computerAI: function(){
             var that = this; //复制this对象
             return (function(){
                 //定义变量，分数统计数组和坐标存储变量
                 var myScore = [],
                     computerScore = [];
                 var max = 0,
                     u = 0, v = 0;
                 //分数统计初始化
                 for(var i=0; i<15; i++){
                     myScore[i] = [];
                     computerScore[i] = [];
                     for(var j=0; j<15; j++){
                         myScore[i][j] = 0;
                         computerScore[i][j] = 0;
                     }
                 }
                 //分数（权重）统计&计算，获取坐标
                 for(var i=0; i<15; i++){
                     for(var j=0; j<15; j++){
                         //判断当前位置是否没有落子
                         if(chessBoard[i][j] == 0){
                             //根据赢法数组计算分数
                             for(var k=0; k<count; k++){
                                 //如果存在第K种赢法的可能性
                                 if(wins[i][j][k]){
                                     if(myWin[k] == 1){
                                         myScore[i][j] += 200;
                                     }else if(myWin[k] == 2){
                                         myScore[i][j] += 400;
                                     }else if(myWin[k] == 3){
                                         myScore[i][j] += 2000;
                                     }else if(myWin[k] == 4){
                                         myScore[i][j] += 10000;
                                     }

                                     if(computerWin[k] == 1){
                                         computerScore[i][j] += 220;
                                     }
                                     else if(computerWin[k] == 2){
                                         computerScore[i][j] += 420;
                                     }
                                     else if(computerWin[k] == 3){
                                         computerScore[i][j] += 2100;
                                     }
                                     else if(computerWin[k] == 4){
                                         computerScore[i][j] += 20000;
                                     }
                                 }
                             }
                             //通过判断获取最优的落子点
                             if(myScore[i][j] > max){
                                 max = myScore[i][j];
                                 u = i;
                                 v = j;
                             }else if(myScore[i][j] == max){
                                 if(computerScore[i][j] > computerScore[u][v]){
                                     u = i;
                                     v = j;
                                 }
                             }

                             if(computerScore[i][j] > max){
                                 max = computerScore[i][j];
                                 u = i;
                                 v = j;
                             }else if(computerScore[i][j] == max){
                                 if(myScore[i][j] > myScore[u][v]){
                                     u = i;
                                     v = j;
                                 }
                             }
                         }
                     }
                 }
                 that.oneStep(u, v, false);  //计算机落子
                 chessBoard[u][v] = 2;  ////玩家白棋落子为2
                 //判断当前落点是否已有棋子，如果没有则落子成功，如果有则后台提示
                 for(var k = 0; k < count; k++){
                     if(wins[u][v][k]){
                         computerWin[k]++;
                         myWin[k] = 999;
                         if(computerWin[k] == 5){
                             window.alert("Computer Win !")
                             over = true;
                         }
                     }
                 }
                 if(over == false){
                     me = !me;
                 }
             })();
         },
     };

     //重新开始
     document.getElementById('restart').onclick = function(){
         window.location.reload();
     }
     //执行代码
     goBang.init();

 })();
