console.dir("index js")

// <th>종목</th>
//                <th>시가총액</th>
//                <th>PER</th>
//                <th>배당율</th>
//                <th>ROE추세</th>
//                <th>주가</th>

function appendTable(target, data_list){
    for(let index=0; index<data_list.length; index++){

        let row = data_list[index];
        let tr = document.createElement("tr")
        let tdStock = createTdATag(row.stock_id, row.stock_name)
        let tdMarketCapital = createTd(row.market_capitalization)
        let tdPer = createTd(row.per)
        let tdDividendRate = createTd(row.dividend_rate)
        let tdRoeList = createTd(row.roe_trends)

        tr.append(tdStock)
        tr.append(tdMarketCapital)
        tr.append(tdPer)
        tr.append(tdDividendRate)
        tr.append(tdRoeList)
        console.dir(tr)
        target.append(tr)
    }
}

function createTdATag(stock_id, stock_name){
    let td = document.createElement("td")
    let naver_finance_url = "https://finance.naver.com/item/main.nhn?code="
    let aTagStock = document.createElement("a")
    aTagStock.setAttribute("href", naver_finance_url + stock_id)
    aTagStock.setAttribute("target", "_blank")
    aTagStock.innerText = stock_name
    td.appendChild(aTagStock)
    return td
}


function make_roi_trend(roi_list){
    let keys = Object.keys(roi_list)
    let range = keys.length
    return (roi_list[keys[0]]*1 - roi_list[keys[1]]*1).toFixed(2)
}


function createTd(column){
    let td = document.createElement("td")
    td.innerText = column
    return td;
}