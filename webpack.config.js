var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    context: __dirname,
    entry: './assets/js/index', 
    
    output: {
        path: path.resolve('./assets/bundles/'), 
        filename: "[name]-[hash].js"
    },
    
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}), 
        //new webpack.optimize.UglifyJsPlugin(),
        //new webpack.optimize.DedupePlugin(),
        // new webpack.DefinePlugin({
        //     'process.env': {
        //         'NODE_ENV': JSON.stringify('production')
        //     }
        // })
    ],
    
    module: {
        loaders: [
            {test: /\.jsx?$/, 
                exclude: /node_modules/, 
                loader: 'babel-loader', 
                query: {
                    presets: ['react'] 
                }
            }
        ]
    },
    
    resolve: {
        modulesDirectories: ['node_modules'],
        extensions: ['', '.js', '.jsx'] 
    }
}
