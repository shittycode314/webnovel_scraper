# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:36:51 2018

@author: Henry
"""
def writeScriptFile():
    file = open('script.js', 'w+')
    file.write('''
        document.onkeydown = function (e) { 
            e = e || window.event; 
            var charCode =  e.keyCode || e.key || e.which; 
            if (charCode == 39)
                document.getElementById('next').click();
            if (charCode == 37)
                document.getElementById('prev').click();
        };
                   
        ''')
    file.close()
    
def writeCssFile():
    file = open('style.css', 'w+')
    file.write('''
        body{
        	width: 800px;
        	padding:50px;
        	font-family: Arial;
        	font-size: 20;
        }
        ''')
    file.close()