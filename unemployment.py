import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import numpy as np
data = pandas.read_csv("unemployment analysis.csv")
unemployment_crs = data.melt(id_vars = ["Country Name", "Country Code"],
         var_name = "Year",
         value_name = "Unemployment Rate")
unemployment_average = unemployment_crs.groupby(["Country Code", "Year"]).mean().unstack()
unemployment_avg = unemployment_average.loc[:, "Unemployment Rate"]
unemployment_avgT = unemployment_avg.transpose()
unemployment_avgTM = unemployment_avgT.loc[:, "AFE":"AZE"]
chart_def = """
{
    chart: {
        type: 'spline',
        marginRight: 130,
        marginBottom: 100
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2021'
    },
    subtitle: {
        align: 'center',
        text: 'According to the Employment Data-Set'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 0,
        y: 0,
        floating: false,
        borderWidth: 2,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        title: {
            text: 'Date'
        },
        plotBands: [{ // Highlight the two last years
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 1990,
            dataLabels: {
            enabled: false,
            inside: true,
            align: 'right'
            }
        },
        spline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048
            ]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of Employment Rate Around the World", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "These graphs represent employment rate analysis", classes = "text-body1 text-weight-bolder text-center")
    hc = jp.HighCharts(a = wp, options = chart_def)
    hc.options.xAxis.categories = list(unemployment_avgTM.index)
    hc.options.yAxis.categories = list(unemployment_avgTM.columns[12:])
    hc.options.title.text = "Average Rating by Country by Year(from Africa Eastern and Southern to Azerbaijan)"
    hc_data = [{"name":v1, "data":[v2 for v2 in unemployment_avgTM[v1]]} for v1 in unemployment_avgTM.columns]
    hc.options.series = hc_data
    
    return wp

jp.justpy(app)