sphinxcontrib-ros紹介
======================

第7回ROS勉強会＠ドワンゴ

by otamachan

(http://otamachan.github.io/slide-sphinxcontrib-ros/)

自己紹介
--------

* Name: Tamaki Nishino
* ID: otamachan (Twitter: otamasan)
* 愛知県在住サラリーマンで3児のお父さん
* ROSは今年の1月から使い始めました
* 勉強会発表初めて枠

  - Tシャツにつられてしまいました・・・
  - Tシャツ駆動開発
  - Tシャツ怖い

ところで
----------

* みなさんはドキュメント書いてますか？
* ドキュメント書くの好きですか？

私は好きではありません
----------------------

ドキュメント書いていたはずなのに、気づいたら、

  * 音声認識で文書生成するプログラム書いてる
  * Texのマクロいじってる
  * Sphinxの拡張書いてる

ことが多々・・・

そんな私ですが、今日はROSのドキュメンテーションツールを紹介します。

目次
----

#. Sphinxの紹介
#. sphinxcontrib-rosの紹介
#. まとめ

まずはSphinxの紹介
------------------

`Sphinx <http://sphinx-users.jp/>`_ とは
  * Pythonで書かれたドキュメンテーションツール
  * reStructuredText(マークアップ言語)でドキュメントを記述
  * HTML, PDF, ePub等出力フォーマットが豊富
  * HTMLのテーマも豊富
  * 多言語対応のドキュメントも書ける
  * `Python <http://docs.python.jp/3/>`_ のドキュメントに使用されている
  * `ReadTheDoc <https://readthedocs.org/>`_ といったホスティングサービスも

こんな感じで書くと
------------------

.. rst-class:: small

.. literalinclude:: _sample/sample.rst
   :language: rst

こんな風にかっこよく出力してくれる
----------------------------------

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/sample.html" frameborder="0"></iframe>
    </div>

良い点(個人的な感想)
---------------------

* 簡単にかっこ良く書ける
* Gitとかで管理しやすい
* Pythonで拡張が書ける!

使いづらい点(個人的な感想)
--------------------------

* 細かい表現がしづらい(表とか)
* WYSIWYGでない(ビルドのタイムラグがある)
* ソフト屋さんでないと敷居が少し高い

ロボット界でもちらほらSphinxが
------------------------------

NAOqi(Pepper)
-------------

* http://doc.aldebaran.com/2-1/index.html

.. raw:: html

    <div>
      <iframe style="height:500px" src="http://doc.aldebaran.com/2-1/index.html" frameborder="0"></iframe>
    </div>

fetch robotics
---------------

* http://docs.fetchrobotics.com/

.. raw:: html

    <div>
      <iframe style="height:500px" src="http://docs.fetchrobotics.com/" frameborder="0"></iframe>
    </div>

Choreonoid
-----------

* http://choreonoid.org/en/

.. raw:: html

    <div>
      <iframe style="height:500px" src="http://choreonoid.org/en/" frameborder="0"></iframe>
    </div>

ROSのドキュメントといえばROS wiki
---------------------------------

.. raw:: html

    <div>
      <iframe style="height:520px" src="http://wiki.ros.org/Documentation" frameborder="0"></iframe>
    </div>

Wiki拡張で書けて
------------------

.. raw:: html

    <div>
      <iframe style="height:520px" src="http://wiki.ros.org/amcl?action=raw" frameborder="0"></iframe>
    </div>

パッケージやAPIを出力してくれる
-------------------------------

.. raw:: html

    <div>
      <iframe style="height:520px" src="http://wiki.ros.org/amcl#line-2" frameborder="0"></iframe>
    </div>

かっこいい
-----------

.. rst-class:: build

* かも

SphinxでもROSのドキュメントかっこよく書きたい
---------------------------------------------

sphinxcontrib-rosの紹介
------------------------

`sphinxcontrib-ros <https://pypi.python.org/pypi/sphinxcontrib-ros>`_
  SphinxでROSのドキュメンテーションをするための拡張

  #. シンタックスハイライト
  #. パッケージ概要
  #. メッセージ定義
  #. インタフェース

  が書ける。

インストール
------------

#. パッケージインストール

   .. code-block:: bash

      $ pip install sphinxcontrib-ros

#. 設定ファイル(``conf.py``)に追加

   .. code-block:: python

      # 拡張の追加
      extenstions += ['sphinxcontrib.ros']
      # パッケージパスを指定
      ros_base_path = ['../src']

(1)シンタックスハイライト
-------------------------

.. rst-class:: small

.. literalinclude:: _sample/syntax.rst
   :language: rst
   :lines: 1-30

出力
----

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/syntax.html" frameborder="0"></iframe>
    </div>

(2)パッケージ概要
------------------

.. literalinclude:: _sample/package.rst
   :language: rst

出力
----

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/package.html" frameborder="0"></iframe>
    </div>

めんどくさい
------------

package.xml
------------

.. literalinclude:: _sample/package.xml
   :language: xml

autopackage
------------

.. literalinclude:: _sample/autopackage.rst
   :language: rst

出力
----

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/autopackage.html" frameborder="0"></iframe>
    </div>

(2)メッセージ定義
-----------------

.. literalinclude:: _sample/message.rst
   :language: rst

出力
----

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/message.html" frameborder="0"></iframe>
    </div>

めんどくさい
------------

GreatAutoMessage.msg
---------------------

.. literalinclude:: _sample/msg/GreatAutoMessage.msg
   :language: rostype
   :lines: 1-30

automessage
------------

.. literalinclude:: _sample/automessage.rst
   :language: rst

出力
----

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/automessage.html" frameborder="0"></iframe>
    </div>

オプションとか
---------------

.. raw:: html

    <div>
      <iframe style="height:520px" src="http://otamachan.github.io/sphinxcontrib-ros/howto.html#directive-ros:automessage" frameborder="0"></iframe>
    </div>

(3)インターフェース定義
------------------------

.. rst-class:: small

.. literalinclude:: _sample/node.rst
   :language: rst

出力例
--------

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/node.html" frameborder="0"></iframe>
    </div>

サンプル
---------

Indigo/Jadeの

* 全パッケージ(1858/664)
* 全メッセージ

を出力してみました。(TravisCI/Ubuntu14.04)

出力
----

.. raw:: html

    <div>
      <iframe style="height:520px" src="http://otamachan.github.io/sphinxros/jade/" frameborder="0"></iframe>
    </div>

自プロジェクトで使う時
----------------------

* 下から全部メッセージ定義していくのめんどくさい

大丈夫
------

* そんな時の `sphinx.ext.intersphinx <http://sphinx-doc.org/latest/ext/intersphinx.html>`_

  ``conf.py`` に

  .. code-block:: python

     extensions += ['sphinx.ext.intersphinx']
     intersphinx_mapping = {'ros':
       ('http://otamachan.github.io/sphinxros/indigo/', None)}

  って書いておけば

適当に参照しても
----------------

.. literalinclude:: _sample/intersphinx.rst
   :language: rst

出力
----

.. raw:: html

    <div>
      <iframe style="height:520px" src="sample/intersphinx.html" frameborder="0"></iframe>
    </div>

まとめ
-------

* Tシャツにつられてsphinxcontrib-rosを公開しました
* conf.pyに以下を追加するだけ

  .. code-block:: python

     extensions += ['sphinxconrib.ros', 'sphinx.ext.intersphinx']
     ros_base_path = ['../src']
     intersphinx_mapping = {'ros':
       ('http://otamachan.github.io/sphinxros/indigo/', None)}

* かっこよくROSのドキュメントが書けちゃうかも

今後のTODO
----------

* ちゃんとsphinxcontrib-rosの **ドキュメント書く**
* テスト真面目に書く
* ``:ros:wiki:`package``` Roleの追加

ありがとうございました
----------------------

* **Hope your happy ROS documentation life with Sphinx!**
* **Any feedback is wellcome!** → `GitHub <https://github.com/otamachan/sphinxcontrib-ros>`_

* ちなみにこのスライドもSphinxで記載しています

  * 拡張: `hieroglyph <https://github.com/nyergler/hieroglyph>`_
  * Source: `github.com <https://github.com/otamachan/sphinxcontrib-ros-slide/blob/master/index.rst>`_
  * Build: `travis-ci.com <https://travis-ci.org/otamachan/sphinxcontrib-ros-slide/>`_
  * Slide: `gitbub.io <http://otamachan.github.io/sphinxcontrib-ros-slide/>`_
