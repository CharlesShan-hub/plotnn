#!/bin/bash

# 检查参数是否为空
if [ $# -eq 0 ]; then
  echo "Usage: $0 <python_script>"
  exit 1
fi

# 记录当前目录
current_dir=$(pwd)

# 拷贝Python脚本到指定目录
cp $1 /Users/kimshan/resources/Tools/PlotNeuralNet/pyexamples

# 进入指定目录
cd /Users/kimshan/resources/Tools/PlotNeuralNet/pyexamples

# 运行Python脚本，并将输出重定向到/dev/null
python $(basename $1) >/dev/null 2>&1

# 生成TeX文件的文件名
tex_file="${1%.py}.tex"

echo $tex_file

# 检查TeX文件是否存在
if [ -f "$tex_file" ]; then
  # 使用pdflatex编译TeX文件
  pdflatex $tex_file

  # 生成PDF文件的文件名
  pdf_file="${tex_file%.tex}.pdf"

  # 检查PDF文件是否生成成功
  if [ -f "$pdf_file" ]; then
    # 将PDF文件拷贝回原文件夹
    cp $pdf_file $current_dir
    echo "PDF file copied to original directory."
  else
    echo "Failed to generate PDF file."
  fi
else
  echo "TeX file not found."
fi

# 返回原来的目录
cd $current_dir
