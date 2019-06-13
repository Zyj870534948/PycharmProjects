function initFilter() {
    var me = this

    this.orderList = new Array()
    this.sesl = new Array()

    this.addOrder = function (order) {
        me.orderList.push(order)
    }
    this.addSQLExpressionSet = function (ses) {
        me.sesl.push(ses)
    }

    this.buildBySe = function (se, order, lop) {
        me.orderList = (typeof order === 'undefined') ? new Array() : (order instanceof Array) ? order : [order]
        var ses = new SQLExpressionSet(lop || 'and', (se instanceof Array) ? se : [se])
        me.sesl.push(ses)
    }

    this.getFilter = function () {
        return {
            orderList: me.orderList,
            sesl: me.sesl
        }
    }
}

function SQLOrder(name, oType) {
    this.property = name
    this.direction = oType
}

function SQLExpressionSet(lop, selist) {
    this.logicalOp = lop
    this.sel = selist
}

function SQLException(lop, name, mathM, exp, ignoreC) {
    /**
     * 表达式逻辑关系符，and，or，not
     *  连接该表达式时的逻辑关系符号
     */
    this.logicalOp = lop
    /**
     * 属性名
     *      String类型
     */
    this.property = name
    /**
     * 匹配方式
     *      String 类型
     */
    this.matchMode = mathM

    /**
     * 匹配的值
     *      Object[] 对象数组
     *      对于matchMode为between和in需要多个值
     */
    if (exp instanceof Array) {
        this.value = exp
    } else {
        this.value = [exp]
    }

    this.ignoreCase = ignoreC || false
}

/**
 * arr参数
 *      Object[] 对象数组
 *      数组中是对象，对象包含两个属性name，value
 *      name参数名称，value参数的值，mathM匹配的值
 *      mathM常用有3个值：'='全匹配（默认），'like'模糊匹配，'between'范围直接（value是数组[1,10]）
 * 例:[{name:'username',value:'admin',mathM:'like'},{name:'password',value:'123456'}]
 */

function SQLFilter(arr) {
    if (!(arr instanceof Array)) {
        return false
    }
    const filter = new initFilter()
    const sel = []
    arr.forEach(function (item) {

        if (item.value !== '') {
            let mathM = '='
            let val = item.value
            if (item.mathM !== undefined && item.mathM !== '') {
                mathM = item.mathM
            }
            if (mathM === 'like') {
                val = '%25' + val + '%25'
            }
            const se = new SQLException('and', item.name, mathM, val, true)
            sel.push(se)
            const ses = new SQLExpressionSet('and', sel)
            filter.addSQLExpressionSet(ses)
        }
    })
    const f = filter.getFilter()
    // console.log(f)
    return JSON.stringify(f)
}

/**
 * arr参数
 *      Object[] 对象数组
 *      数组中是对象，对象包含两个属性name，value
 *      name参数名称，value参数的值
 *      value的值有desc(降序)、asc(升序)
 * 例:[{name:'id',value:'desc'}]
 */
function SQLOrder(arr) {
    if (!(arr instanceof Array)) {
        return false
    }
    const sort = []
    arr.forEach(function (item) {
        if (item.value !== '') {
            const obj = {
                property: item.name,
                direction: item.value
            }
            sort.push(obj)
        }
    })
    return JSON.stringify(sort)
}
