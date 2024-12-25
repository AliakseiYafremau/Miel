const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index.jsx",
    mode: "development",
    devServer: {
        static: './src',
        historyApiFallback: true
    },
    output: {
        path: path.join(__dirname, "/dist"),
        publicPath: '/',
        filename: "main.js",
    },
    module: {
        rules: [
            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            },
            {
              test: /\.(png|jpe?g|gif|svg|ico)$/i,
              use: [
                {
                  loader: 'file-loader',
                },
              ],
            },
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html"
        })
    ]
}