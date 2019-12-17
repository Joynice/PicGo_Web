layui.use(['upload', 'table'], function () {
    var $ = layui.$;
    var token = $("meta[name='csrf-token']").attr('content');
    var upload = layui.upload;
    var table = layui.table;

    //图片上传
        upload.render({
        elem: '#headImg' //绑定元素
        , url: '/images/' //上传接口
        , method: 'post'
        , headers: {'X-CSRF-TOKEN': token}
        , size: 1024 * 10 //图片最大10M
        , accept: 'images'
        , done: function (res) {
            //上传完毕回调
            if (res.code === 0) {
                layer.msg(res.message);

            } else {
                return layer.msg(res.message);
            }
        }
        , error: function () {
            //请求异常回调
        }
    });

});