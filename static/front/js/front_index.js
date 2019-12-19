layui.use(['upload', 'flow','layer'], function () {
    var $ = layui.$;
    var token = $("meta[name='csrf-token']").attr('content');
    var upload = layui.upload;
    var flow = layui.flow;
    flow.lazyimg();

    layer.photos({
        photos: '.show_div'
        , anim: 5 //0-6的选择，指定弹出图片动画类型，默认随机（请注意，3.0之前的版本用shift参数）
    });


    //图片上传
    upload.render({
        elem: '#headImg' //绑定元素
        , url: '/images/' //上传接口
        , method: 'post'
        , headers: {'X-CSRF-TOKEN': token}
        , size: 1024 * 10 //图片最大10M
        , accept: 'images'
        , before: function () {
            layer.load(0, {shade: false});
        }
        , done: function (res) {
            //上传完毕回调
            layer.closeAll('loading');
            if (res.code === 0) {
                data = res.data;
                var link = data.link;
                var id = data.id;
               //todo:将上传添加到历史上传
                $("#show").css('display', '');
                $("#show_div img").attr('src', link);
                $("#show_btn #copy").attr({'data-clipboard-text':link});
                $("#show_btn .delete").attr({'data-id': id});
                layer.msg(res.message);

            } else {
                return layer.msg(res.message);
            }
        }
        , error: function () {
            //请求异常回调
            layer.closeAll('loading');
        }
    });

});

