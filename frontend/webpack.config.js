const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index.jsx",
    mode: "production",
    performance: {
        hints: false
    },
    devServer: {
        static: './src',
        historyApiFallback: true,
        port: 3000
    },
    output: {
        path: path.join(__dirname, "/build"),
        publicPath: '/',
        filename: "main.js",
        assetModuleFilename: path.join('images', '[name].[contenthash][ext]')
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
                test: /\.(png|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html",
            favicon: "./src/resource/assets/favicon.ico"
        })
    ]
}