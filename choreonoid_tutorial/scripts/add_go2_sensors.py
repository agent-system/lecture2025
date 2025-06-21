import cnoid.Base
import cnoid.Body
import cnoid.BodyPlugin
import cnoid.Util

item_tree_view = cnoid.Base.ItemTreeView.instance
root_item = cnoid.Base.RootItem.instance

item_name = "go2_description"
go2_item = root_item.findItem(item_name)
if not go2_item:
    print(f"Not found Item: {item_name}")
else:
    body = go2_item.body

    # 追加するカメラの情報
    camera = cnoid.Body.Camera()
    camera.name = "camera"
    camera.width = 640
    camera.height = 480
    camera.fieldOfView = 1.39626  # 約80度
    camera.nearClipDistance = 0.01
    camera.farClipDistance = 10.0

    # 取り付け先のリンク
    link = body.link("camera_link")
    if not link:
        print("camera_link が Body に見つかりません。")
    else:
        camera.setLink(link)
        camera.setLocalTranslation([0, 0, 0])  # camera_link原点に取り付け
        camera.setLocalRotation(cnoid.Util.AngleAxis(0, [0, 0, 1]))  # 向きは必要に応じて調整
        link.addDevice(camera)
        camera.notifyStateChange()

        # GUIに変更を通知（保存や表示のため）
        go2_item.notifyModelUpdate()
        print("camera デバイスを追加しました。")
