import discord 
import random





TOKEN = 'ODc2NDM3MjI3MDQ2MDYwMDcy.YRkDxg._bxZKE3Ckd2i9mkKu7xFC-Rj-6k'

ARABIC_QUESTIONS = [
    "من هو بيت أسرارك؟",
    "من هو الشخص الذي يمكن لك أن تعتمد عليه؟",
    "من هو الشخص القادر على معرفة ما تشعر به أنت من نظرة واحدة.؟",
    "من هو الشخص الذي تستطيع معرفة مشاعره من نظرة واحدة؟",
    "من هو العدو الحالي الذي كان صديق؟",
    "من هو الشخص الذي يدين لك باعتذار؟",
    "من هو الشخص الذي ستقدم له باقة من الأزهار؟",
    "من هو الشخص الذي ستقدم له باقة من الشوك؟",
    "من هو الشخص الذي كنت تثق به وأثبت أنه أهل للثقة؟",
    "من هو الشخص الذي كنت تثق به واثبت أنه لا يستحق ذلك؟",
    "من هو الشخص الذي كنت لا تثق به أبدًا وأثبت أنه يستحق ثقتك؟",
    "من هو أول شخص تعرفت عليه في العمل أو الجامعة أو المدرسة؟",
    "من هو الشخص الذي يعرف عنك الكثير من المعلومات؟",
    "من هو الشخص الذي تعتبره أخ لك؟",
    "من هو الشخص الذي علمك الكثير؟",
    "من هو الشخص الذي قام بتغيير نظرتك إلى الحياة؟",
    "من هو الشخص الذي تفرح لفرحه وتحزن لحزنه؟",
    "من هو الشخص الذي تتنافس معه؟",
    "ما هو الشيء الذي لا يمكنك التخلي عنه أبدًا؟",
    "ما هي الكلمات التي لا يمكنك توجيهها للشخص الذي تحبه؟",
    "ما هو أول شيء تفكر به عندما تغمض عينيك؟",
    "ما هي الأمنية التي تتمنى امتلاك مصباح علاء الدين لتحقيقها؟",
    "ما هو التصرف الذي ندمت أنك قمت به؟",
    "ما هي الذكرة التي تحتاج إلى نسيانها؟",
    "ما هو التصرف الذي ندمت أنك لم تقم به؟",
    "ما هي الهدية التي تحتاجها أكثر من أي شيء آخر؟",
    "ما هو الطعام والشراب واللون المفضل بالنسبة لصديقك المقرب؟",
    "ما هي الدولة التي تتمنى العيش فيها؟",
    "ما هو اسم الكتاب المناسب لو كان يحكي قصة حياتك؟",
    "ما هي الأغنية التي تصف مشاعرك هذه الفترة؟",
    "ما هو تاريخ اليوم الذي لا يمكنك نسيانه أبدًا؟",
    "ما هي التصرفات المضحكة التي أخبرتك والدتك أنك قمت بها في صغرك؟",
    "ما هو الاسم الذي يطلقه عليك أصدقائك المقربين؟",
    "ما هي الأسماء التي ستطلقها على أبنائك وبناتك؟",
    "ما هو الاسم الذي تود أن يكون بدلًا من اسمك الحالي؟",
    "ما هي الصفات التي تعتقد أنها تميزك؟",
    "ما هو أكثر شيء تود الحصول عليه؟",
    "ما هي الحياة المثالية بالنسبة لك؟",
    "كم مرة شعرت فيها بأنك وحيد بشكل كامل على الرغم من كل من حولك؟",
    "كم مرة ندمت على أمر قمت به أو كلمات قلتها؟",
    "كم مرة ندمت على أمر لم تقم به أو كلمات لم تقلها؟",
    "كم مرة شعرت بالظلم؟",
    "كم مرة شعرت أنك ظالم؟",
    "كم مرة بكيت أمام الشخص المقرب منك؟",
    "كم مرة تمنيت العودة في الزمن للخلف؟",
    "كم مرة شعرت أنك متعب من كل شيء؟",
    "كم مرة ضحكت من قلبك وشعرت بسعادة كبيرة؟",
    "كم مرة تمكنت من التحكم بغضبك؟",
    "كم مرة لم تتمكن من السيطرة على الغضب؟",
    "كم مرة تتناول القهوة في اليوم الواحد؟",
    "كم مرة حضرت الطعام لنفسك؟",
    "كم مرة قمت بإحراق الطعام أثناء إعداده؟",
    "كم مرة كذبت كذبة بيضاء؟",
    "كم مرة قلت الحقيقة وكانت جارحة؟",
    "كم مرة قمت بالتخلي عن شيء تريده بشدة؟",
    "كم مرة تمكنت من الوصول إلى هدفك؟",
    "كم مرة نمت في أثناء انشغالك بالعمل الشديد؟",
    "كم مرة نسيت أن تأكل؟",
    "هل أنت شخص واثق من نفسه أم تحتاج لتقوية ثقتك بنفسك؟",
    "هل أنت شخص يتمتع بالروح الرياضية أم يمكنك بسهولة الغضب عند الخسارة؟",
    "هل أنت شخص عنيد حول ما تريد أم تستسلم بعد أول محاولة؟",
    "هل أنت شخص كتوم يحفظ الأسرار أم أنك لا تقدر على الاحتفاظ بسر؟",
    "هل أنت من الأشخاص الذين يفكرون قبل النوم بما قاموا به سابقًا أو من الأشخاص الذين يفكرون بالأشياء التي سيقومن فيها غدًا؟",
    "هل أنت شخص يحب الطعام أم أنك تجد أنه أمر ثانوي؟",
    "هل أنت شخص مدخن أو كنت مدخن أو لم تدخن في حياتك أبدًا؟",
    "هل أنت شخص هادئ بطبعه أم أنك صاخب؟",
    "هل أنت شخص يمكنه أن يضحك بسهولة أم أن الأشياء التي تضحكك قليلة؟",
    "هل أنت شخصية جذابة وتتمتع بالكاريزما أم أنك شخصية خجولة منطوية؟",
    "هل أنت شخص يحب الاجتماع بالناس أم تفضل الوحدة في عالمك الخاص؟",
    "هل أنت تفضل قراءة الروايات أم مشاهدة الأفلام؟",
    "هل أنت شخص واقعي أم رومنسي؟",
    "هل أنت تؤمن بالصدف أم لا تعتقد بها؟",
    "هل أنت واقع بالحب أم أنك لا تعتقد أنه موجود أصلًا؟",
    "هل أنت شخص متفهم أم أنك صاحب رأي جامد؟",
    "هل أنت تتمتع بشخصية تناسب عمرك أم شخصية أكبر من عمرك؟",
    "هل أنت متواضع أم مغرور متكبر؟",
    "هل أنت شخص سريع البكاء أم تعتقد أن البكاء للضعفاء؟",
    "هل أنت شخص قادر على إخفاء مشاعره؟",

]
ENGLISH_QUESTIONS = [
    "When was the last time you lied?",
    "When was the last time you cried?",
    "What's your biggest fear?",
    "What's your biggest fantasy?",
    "Do you have any fetishes?",
    "What's something you're glad your mum doesn't know about you?",
    "Have you ever cheated on someone?",
    "What's the worst thing you've ever done?",
    "What's a secret you've never told anyone?",
    "Do you have a hidden talent?",
    "Who was your first celebrity crush?",
    "What are your thoughts on polyamory?",
    "What's the worst intimate experience you've ever had?",
    "What's the best intimate experience you've ever had?",
    "Have you ever cheated in an exam?",
    "What's the most drunk you've ever been?",
    "Have you ever broken the law?",
    "What's the most embarrassing thing you've ever done?",
    "What's your biggest insecurity?",
    "Have you ever stayed friends with someone because it benefitted you beyond just the friendship?",
    "What's the biggest mistake you've ever made?",
    "What's the most disgusting thing you've ever done?",
    "Who would you like to kiss in this room?",
    "What's one thing you hate people knowing about you?",
    "What's the worst thing anyone's ever done to you?",
    "What's the best thing anyone's ever done for you?",
    "Have you ever had a run in with the law?",
    "What's your worst habit?",
    "What's the most embarrassing thing you've done in a taxi?",
    "What's the worst thing you've ever said to anyone?",
    "Have you ever peed in the shower?",
    "What's the strangest dream you've had?",
    "Have you ever been caught doing something you shouldn't have?",
    "What's the worst date you've been on?",
    "What's the best date you've been on?",
    "What happened on the latest night out you've ever had?",
    "What's your biggest regret?",
    "What's the biggest misconception about you?",
    "Have you ever said something you regret about someone in this room?",
    "What's one thing you wish people knew about you?",
    "Where's the weirdest place you've had sex?",
    "Why did your last relationship break down?",
    "Have you ever lied to get out of a bad date?",
    "What's the most trouble you've been in?",
    "When did you last have sex outside?",
    "What's the worst thing you've lied about?",
    "What's one thing you wish you'd lied about?",
    "What's the best piece of advice you've been given?",
    "What's the most you've spent on a night out?",
    "Name a time you think you were a bad partner",
    "What's your guilty pleasure?",
    "What's one thing you only do when you're alone?",
    "If you had to get back with an ex, who would you choose?",
    "If you had to cut one friend out of your life, who would it be?",
    "Do you have a favourite friend?",
    "Do you have a favourite sibling?",
    "What's the strangest rumour you've heard about yourself?",
    "What's your biggest turn on?",
    "What's the silliest reason you've left a club early?",
    "What have you purchased that's been the biggest waste of money?",
    "If you could swap lives with someone in this room, who would it be?",

]
client = discord.Client()



@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    botactivity = discord.Activity(type=discord.ActivityType.playing, name="Scraping your questions c!help")
    await client.change_presence(activity=botactivity, status=discord.Status.do_not_disturb)
    
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_msg} ({channel})')
    if message.author == client.user:
        return
    if message.channel.name == 'event-chat':
        #if user_msg.lower()=='hello':
            #await message.channel.send(f'hello {username}')
        #elif user_msg.lower()=='bye':
            #await message.channel.send(f'bye {username}')
        #elif user_msg.lower() == '!random':
            #respone = f'This is your random number : {random.randrange(100000000)}'
            #await message.channel.send(respone)
            #return
        if user_msg.lower() == "ar!question":
            question = random.choice(ARABIC_QUESTIONS)
            await message.channel.send(question)
            return
        elif user_msg.lower() == "en!question":
            question = random.choice(ENGLISH_QUESTIONS)
            await message.channel.send(question)
            return
        elif user_msg.lower() == "c!help":
            embed=discord.Embed(title="Confessional Help", url="https://discord.com/api/oauth2/authorize?client_id=876437227046060072&permissions=259846043712&scope=bot", description="This is an embed that will show how to build an embed and the different components", color=0x000000)
            embed.set_author(name=message.author)
            
            embed.add_field(name='**ar!question**',
                            value='*Generates a question in Arabic*', inline=False)
            embed.add_field(name='**en!question**',
                            value='*Generates a question in English*', inline=False)
            embed.set_footer(
                text="Thank You for using our bot")
            await message.reply(embed=embed)
            return
    #if user_msg.lower() == '!anywhere':
       # await message.channel.send("test")
        #return


client.run(TOKEN)
