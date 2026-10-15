@echo off

mkdir locales 2>nul

(
echo {
echo   "next_chapter": "下一章",
echo   "next_page": "下一页",
echo   "previous_chapter": "上一章",
echo   "previous_page": "上一页",
echo   "popular_rank": "热门榜",
echo   "recommended_novels": "热门小说推荐"
echo }
)>locales\zh-CN.json


(
echo {
echo   "next_chapter": "下一章",
echo   "next_page": "下一页",
echo   "previous_chapter": "上一章",
echo   "previous_page": "上一页",
echo   "popular_rank": "熱門榜",
echo   "recommended_novels": "熱門小說推薦"
echo }
)>locales\zh-TW.json


(
echo {
echo   "next_chapter": "Next Chapter",
echo   "next_page": "Next Page",
echo   "previous_chapter": "Previous Chapter",
echo   "previous_page": "Previous Page",
echo   "popular_rank": "Popular Ranking",
echo   "recommended_novels": "Popular Novel Recommendations"
echo }
)>locales\en-US.json


(
echo {
echo   "next_chapter": "次の章",
echo   "next_page": "次のページ",
echo   "previous_chapter": "前の章",
echo   "previous_page": "前のページ",
echo   "popular_rank": "人気ランキング",
echo   "recommended_novels": "人気小説おすすめ"
echo }
)>locales\ja-JP.json


(
echo {
echo   "next_chapter": "다음 장",
echo   "next_page": "다음 페이지",
echo   "previous_chapter": "이전 장",
echo   "previous_page": "이전 페이지",
echo   "popular_rank": "인기 순위",
echo   "recommended_novels": "인기 소설 추천"
echo }
)>locales\ko-KR.json


(
echo {
echo   "next_chapter": "Chương tiếp theo",
echo   "next_page": "Trang tiếp theo",
echo   "previous_chapter": "Chương trước",
echo   "previous_page": "Trang trước",
echo   "popular_rank": "Bảng xếp hạng phổ biến",
echo   "recommended_novels": "Đề xuất tiểu thuyết nổi tiếng"
echo }
)>locales\vi-VN.json


(
echo {
echo   "next_chapter": "บทถัดไป",
echo   "next_page": "หน้าถัดไป",
echo   "previous_chapter": "บทก่อนหน้า",
echo   "previous_page": "หน้าก่อนหน้า",
echo   "popular_rank": "อันดับยอดนิยม",
echo   "recommended_novels": "นิยายยอดนิยมแนะนำ"
echo }
)>locales\th-TH.json


(
echo {
echo   "next_chapter": "Bab Berikutnya",
echo   "next_page": "Halaman Berikutnya",
echo   "previous_chapter": "Bab Sebelumnya",
echo   "previous_page": "Halaman Sebelumnya",
echo   "popular_rank": "Peringkat Populer",
echo   "recommended_novels": "Rekomendasi Novel Populer"
echo }
)>locales\id-ID.json


(
echo {
echo   "next_chapter": "Следующая глава",
echo   "next_page": "Следующая страница",
echo   "previous_chapter": "Предыдущая глава",
echo   "previous_page": "Предыдущая страница",
echo   "popular_rank": "Популярный рейтинг",
echo   "recommended_novels": "Рекомендованные популярные романы"
echo }
)>locales\ru-RU.json


(
echo {
echo   "next_chapter": "Siguiente capítulo",
echo   "next_page": "Página siguiente",
echo   "previous_chapter": "Capítulo anterior",
echo   "previous_page": "Página anterior",
echo   "popular_rank": "Ranking popular",
echo   "recommended_novels": "Recomendaciones de novelas populares"
echo }
)>locales\es-ES.json


echo Language files created.
pause