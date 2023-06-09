PGDMP                         {            javie    15.2    15.2 e    q           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            r           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            s           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            t           1262    27645    javie    DATABASE     |   CREATE DATABASE javie WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Guatemala.1252';
    DROP DATABASE javie;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            u           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1255    27782    registrar_bitacora()    FUNCTION     �   CREATE FUNCTION public.registrar_bitacora() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO Bitacora (fechaMod, usuario, modificacion,anterior,nuevo)
	VALUES (now(), 'postgres', TG_OP, old, new);
	RETURN NEW;
END;
$$;
 +   DROP FUNCTION public.registrar_bitacora();
       public          postgres    false    4            �            1259    27793    bitacora    TABLE     �   CREATE TABLE public.bitacora (
    fechamod timestamp without time zone,
    usuario character varying(30),
    modificacion text,
    anterior text,
    nuevo text
);
    DROP TABLE public.bitacora;
       public         heap    postgres    false    4            �            1259    27694 	   bodeguero    TABLE     �   CREATE TABLE public.bodeguero (
    idbodeguero integer NOT NULL,
    nombre character varying(50) NOT NULL,
    idusuario integer NOT NULL,
    idlugarmedico integer NOT NULL
);
    DROP TABLE public.bodeguero;
       public         heap    postgres    false    4            �            1259    27693    bodeguero_idbodeguero_seq    SEQUENCE     �   CREATE SEQUENCE public.bodeguero_idbodeguero_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.bodeguero_idbodeguero_seq;
       public          postgres    false    4    225            v           0    0    bodeguero_idbodeguero_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.bodeguero_idbodeguero_seq OWNED BY public.bodeguero.idbodeguero;
          public          postgres    false    224            �            1259    27733 
   enfermedad    TABLE     q   CREATE TABLE public.enfermedad (
    idenfermedad integer NOT NULL,
    nombre character varying(50) NOT NULL
);
    DROP TABLE public.enfermedad;
       public         heap    postgres    false    4            �            1259    27732    enfermedad_idenfermedad_seq    SEQUENCE     �   CREATE SEQUENCE public.enfermedad_idenfermedad_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.enfermedad_idenfermedad_seq;
       public          postgres    false    4    229            w           0    0    enfermedad_idenfermedad_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.enfermedad_idenfermedad_seq OWNED BY public.enfermedad.idenfermedad;
          public          postgres    false    228            �            1259    27656    especialidad    TABLE     u   CREATE TABLE public.especialidad (
    idespecialidad integer NOT NULL,
    nombre character varying(50) NOT NULL
);
     DROP TABLE public.especialidad;
       public         heap    postgres    false    4            �            1259    27655    especialidad_idespecialidad_seq    SEQUENCE     �   CREATE SEQUENCE public.especialidad_idespecialidad_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.especialidad_idespecialidad_seq;
       public          postgres    false    217    4            x           0    0    especialidad_idespecialidad_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.especialidad_idespecialidad_seq OWNED BY public.especialidad.idespecialidad;
          public          postgres    false    216            �            1259    27749    historialmedico    TABLE     o  CREATE TABLE public.historialmedico (
    idhistorial integer NOT NULL,
    fecha date NOT NULL,
    herencias text,
    tratamiento integer,
    cantidadmedicamento integer,
    estado character varying(20),
    comentario text,
    idlugarmedico integer NOT NULL,
    idpaciente integer NOT NULL,
    idenfermedad integer NOT NULL,
    idmedico integer NOT NULL
);
 #   DROP TABLE public.historialmedico;
       public         heap    postgres    false    4            �            1259    27748    historialmedico_idhistorial_seq    SEQUENCE     �   CREATE SEQUENCE public.historialmedico_idhistorial_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.historialmedico_idhistorial_seq;
       public          postgres    false    233    4            y           0    0    historialmedico_idhistorial_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.historialmedico_idhistorial_seq OWNED BY public.historialmedico.idhistorial;
          public          postgres    false    232            �            1259    27677 
   inventario    TABLE     �   CREATE TABLE public.inventario (
    idinventario integer NOT NULL,
    cantidad integer NOT NULL,
    expiracion date NOT NULL,
    idlugarmedico integer NOT NULL,
    idsuministro integer NOT NULL
);
    DROP TABLE public.inventario;
       public         heap    postgres    false    4            �            1259    27676    inventario_idinventario_seq    SEQUENCE     �   CREATE SEQUENCE public.inventario_idinventario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.inventario_idinventario_seq;
       public          postgres    false    4    223            z           0    0    inventario_idinventario_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.inventario_idinventario_seq OWNED BY public.inventario.idinventario;
          public          postgres    false    222            �            1259    27663    lugarmedico    TABLE     �   CREATE TABLE public.lugarmedico (
    idlugarmedico integer NOT NULL,
    nombre character varying(100) NOT NULL,
    localizacion character varying(100) NOT NULL
);
    DROP TABLE public.lugarmedico;
       public         heap    postgres    false    4            �            1259    27662    lugarmedico_idlugarmedico_seq    SEQUENCE     �   CREATE SEQUENCE public.lugarmedico_idlugarmedico_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.lugarmedico_idlugarmedico_seq;
       public          postgres    false    219    4            {           0    0    lugarmedico_idlugarmedico_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.lugarmedico_idlugarmedico_seq OWNED BY public.lugarmedico.idlugarmedico;
          public          postgres    false    218            �            1259    27711    medico    TABLE     _  CREATE TABLE public.medico (
    idmedico integer NOT NULL,
    nombre character varying(50) NOT NULL,
    direccion character varying(100) NOT NULL,
    telefono character varying(20) NOT NULL,
    numcolegiado character varying(50) NOT NULL,
    idusuario integer NOT NULL,
    idespecialidad integer NOT NULL,
    idlugarmedico integer NOT NULL
);
    DROP TABLE public.medico;
       public         heap    postgres    false    4            �            1259    27710    medico_idmedico_seq    SEQUENCE     �   CREATE SEQUENCE public.medico_idmedico_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.medico_idmedico_seq;
       public          postgres    false    4    227            |           0    0    medico_idmedico_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.medico_idmedico_seq OWNED BY public.medico.idmedico;
          public          postgres    false    226            �            1259    27740    paciente    TABLE       CREATE TABLE public.paciente (
    idpaciente integer NOT NULL,
    nombre character varying(50) NOT NULL,
    direccion character varying(100) NOT NULL,
    telefono character varying(20) NOT NULL,
    masacorporal integer NOT NULL,
    altura integer NOT NULL,
    adicciones text
);
    DROP TABLE public.paciente;
       public         heap    postgres    false    4            �            1259    27739    paciente_idpaciente_seq    SEQUENCE     �   CREATE SEQUENCE public.paciente_idpaciente_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.paciente_idpaciente_seq;
       public          postgres    false    231    4            }           0    0    paciente_idpaciente_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.paciente_idpaciente_seq OWNED BY public.paciente.idpaciente;
          public          postgres    false    230            �            1259    27670 
   suministro    TABLE     q   CREATE TABLE public.suministro (
    idsuministro integer NOT NULL,
    nombre character varying(50) NOT NULL
);
    DROP TABLE public.suministro;
       public         heap    postgres    false    4            �            1259    27669    suministro_idsuministro_seq    SEQUENCE     �   CREATE SEQUENCE public.suministro_idsuministro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.suministro_idsuministro_seq;
       public          postgres    false    4    221            ~           0    0    suministro_idsuministro_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.suministro_idsuministro_seq OWNED BY public.suministro.idsuministro;
          public          postgres    false    220            �            1259    27647    usuario    TABLE     �   CREATE TABLE public.usuario (
    idusuario integer NOT NULL,
    usuario character varying(50) NOT NULL,
    contrasena character varying(50) NOT NULL,
    tipousuario character varying(1) NOT NULL
);
    DROP TABLE public.usuario;
       public         heap    postgres    false    4            �            1259    27646    usuario_idusuario_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_idusuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.usuario_idusuario_seq;
       public          postgres    false    4    215                       0    0    usuario_idusuario_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.usuario_idusuario_seq OWNED BY public.usuario.idusuario;
          public          postgres    false    214            �           2604    27697    bodeguero idbodeguero    DEFAULT     ~   ALTER TABLE ONLY public.bodeguero ALTER COLUMN idbodeguero SET DEFAULT nextval('public.bodeguero_idbodeguero_seq'::regclass);
 D   ALTER TABLE public.bodeguero ALTER COLUMN idbodeguero DROP DEFAULT;
       public          postgres    false    225    224    225            �           2604    27736    enfermedad idenfermedad    DEFAULT     �   ALTER TABLE ONLY public.enfermedad ALTER COLUMN idenfermedad SET DEFAULT nextval('public.enfermedad_idenfermedad_seq'::regclass);
 F   ALTER TABLE public.enfermedad ALTER COLUMN idenfermedad DROP DEFAULT;
       public          postgres    false    228    229    229            �           2604    27659    especialidad idespecialidad    DEFAULT     �   ALTER TABLE ONLY public.especialidad ALTER COLUMN idespecialidad SET DEFAULT nextval('public.especialidad_idespecialidad_seq'::regclass);
 J   ALTER TABLE public.especialidad ALTER COLUMN idespecialidad DROP DEFAULT;
       public          postgres    false    217    216    217            �           2604    27752    historialmedico idhistorial    DEFAULT     �   ALTER TABLE ONLY public.historialmedico ALTER COLUMN idhistorial SET DEFAULT nextval('public.historialmedico_idhistorial_seq'::regclass);
 J   ALTER TABLE public.historialmedico ALTER COLUMN idhistorial DROP DEFAULT;
       public          postgres    false    232    233    233            �           2604    27680    inventario idinventario    DEFAULT     �   ALTER TABLE ONLY public.inventario ALTER COLUMN idinventario SET DEFAULT nextval('public.inventario_idinventario_seq'::regclass);
 F   ALTER TABLE public.inventario ALTER COLUMN idinventario DROP DEFAULT;
       public          postgres    false    222    223    223            �           2604    27666    lugarmedico idlugarmedico    DEFAULT     �   ALTER TABLE ONLY public.lugarmedico ALTER COLUMN idlugarmedico SET DEFAULT nextval('public.lugarmedico_idlugarmedico_seq'::regclass);
 H   ALTER TABLE public.lugarmedico ALTER COLUMN idlugarmedico DROP DEFAULT;
       public          postgres    false    219    218    219            �           2604    27714    medico idmedico    DEFAULT     r   ALTER TABLE ONLY public.medico ALTER COLUMN idmedico SET DEFAULT nextval('public.medico_idmedico_seq'::regclass);
 >   ALTER TABLE public.medico ALTER COLUMN idmedico DROP DEFAULT;
       public          postgres    false    227    226    227            �           2604    27743    paciente idpaciente    DEFAULT     z   ALTER TABLE ONLY public.paciente ALTER COLUMN idpaciente SET DEFAULT nextval('public.paciente_idpaciente_seq'::regclass);
 B   ALTER TABLE public.paciente ALTER COLUMN idpaciente DROP DEFAULT;
       public          postgres    false    231    230    231            �           2604    27673    suministro idsuministro    DEFAULT     �   ALTER TABLE ONLY public.suministro ALTER COLUMN idsuministro SET DEFAULT nextval('public.suministro_idsuministro_seq'::regclass);
 F   ALTER TABLE public.suministro ALTER COLUMN idsuministro DROP DEFAULT;
       public          postgres    false    220    221    221            �           2604    27650    usuario idusuario    DEFAULT     v   ALTER TABLE ONLY public.usuario ALTER COLUMN idusuario SET DEFAULT nextval('public.usuario_idusuario_seq'::regclass);
 @   ALTER TABLE public.usuario ALTER COLUMN idusuario DROP DEFAULT;
       public          postgres    false    215    214    215            n          0    27793    bitacora 
   TABLE DATA           T   COPY public.bitacora (fechamod, usuario, modificacion, anterior, nuevo) FROM stdin;
    public          postgres    false    234   �|       e          0    27694 	   bodeguero 
   TABLE DATA           R   COPY public.bodeguero (idbodeguero, nombre, idusuario, idlugarmedico) FROM stdin;
    public          postgres    false    225   �~       i          0    27733 
   enfermedad 
   TABLE DATA           :   COPY public.enfermedad (idenfermedad, nombre) FROM stdin;
    public          postgres    false    229   �~       ]          0    27656    especialidad 
   TABLE DATA           >   COPY public.especialidad (idespecialidad, nombre) FROM stdin;
    public          postgres    false    217   ,       m          0    27749    historialmedico 
   TABLE DATA           �   COPY public.historialmedico (idhistorial, fecha, herencias, tratamiento, cantidadmedicamento, estado, comentario, idlugarmedico, idpaciente, idenfermedad, idmedico) FROM stdin;
    public          postgres    false    233   s       c          0    27677 
   inventario 
   TABLE DATA           e   COPY public.inventario (idinventario, cantidad, expiracion, idlugarmedico, idsuministro) FROM stdin;
    public          postgres    false    223   �       _          0    27663    lugarmedico 
   TABLE DATA           J   COPY public.lugarmedico (idlugarmedico, nombre, localizacion) FROM stdin;
    public          postgres    false    219   g�       g          0    27711    medico 
   TABLE DATA              COPY public.medico (idmedico, nombre, direccion, telefono, numcolegiado, idusuario, idespecialidad, idlugarmedico) FROM stdin;
    public          postgres    false    227   ��       k          0    27740    paciente 
   TABLE DATA           m   COPY public.paciente (idpaciente, nombre, direccion, telefono, masacorporal, altura, adicciones) FROM stdin;
    public          postgres    false    231   ]�       a          0    27670 
   suministro 
   TABLE DATA           :   COPY public.suministro (idsuministro, nombre) FROM stdin;
    public          postgres    false    221   �       [          0    27647    usuario 
   TABLE DATA           N   COPY public.usuario (idusuario, usuario, contrasena, tipousuario) FROM stdin;
    public          postgres    false    215   S�       �           0    0    bodeguero_idbodeguero_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.bodeguero_idbodeguero_seq', 2, true);
          public          postgres    false    224            �           0    0    enfermedad_idenfermedad_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.enfermedad_idenfermedad_seq', 3, true);
          public          postgres    false    228            �           0    0    especialidad_idespecialidad_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.especialidad_idespecialidad_seq', 6, true);
          public          postgres    false    216            �           0    0    historialmedico_idhistorial_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.historialmedico_idhistorial_seq', 5, true);
          public          postgres    false    232            �           0    0    inventario_idinventario_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.inventario_idinventario_seq', 15, true);
          public          postgres    false    222            �           0    0    lugarmedico_idlugarmedico_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.lugarmedico_idlugarmedico_seq', 6, true);
          public          postgres    false    218            �           0    0    medico_idmedico_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.medico_idmedico_seq', 2, true);
          public          postgres    false    226            �           0    0    paciente_idpaciente_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.paciente_idpaciente_seq', 4, true);
          public          postgres    false    230            �           0    0    suministro_idsuministro_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.suministro_idsuministro_seq', 3, true);
          public          postgres    false    220            �           0    0    usuario_idusuario_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.usuario_idusuario_seq', 5, true);
          public          postgres    false    214            �           2606    27699    bodeguero bodeguero_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.bodeguero
    ADD CONSTRAINT bodeguero_pkey PRIMARY KEY (idbodeguero);
 B   ALTER TABLE ONLY public.bodeguero DROP CONSTRAINT bodeguero_pkey;
       public            postgres    false    225            �           2606    27738    enfermedad enfermedad_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.enfermedad
    ADD CONSTRAINT enfermedad_pkey PRIMARY KEY (idenfermedad);
 D   ALTER TABLE ONLY public.enfermedad DROP CONSTRAINT enfermedad_pkey;
       public            postgres    false    229            �           2606    27661    especialidad especialidad_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.especialidad
    ADD CONSTRAINT especialidad_pkey PRIMARY KEY (idespecialidad);
 H   ALTER TABLE ONLY public.especialidad DROP CONSTRAINT especialidad_pkey;
       public            postgres    false    217            �           2606    27756 $   historialmedico historialmedico_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.historialmedico
    ADD CONSTRAINT historialmedico_pkey PRIMARY KEY (idhistorial);
 N   ALTER TABLE ONLY public.historialmedico DROP CONSTRAINT historialmedico_pkey;
       public            postgres    false    233            �           2606    27682    inventario inventario_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_pkey PRIMARY KEY (idinventario);
 D   ALTER TABLE ONLY public.inventario DROP CONSTRAINT inventario_pkey;
       public            postgres    false    223            �           2606    27668    lugarmedico lugarmedico_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.lugarmedico
    ADD CONSTRAINT lugarmedico_pkey PRIMARY KEY (idlugarmedico);
 F   ALTER TABLE ONLY public.lugarmedico DROP CONSTRAINT lugarmedico_pkey;
       public            postgres    false    219            �           2606    27716    medico medico_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_pkey PRIMARY KEY (idmedico);
 <   ALTER TABLE ONLY public.medico DROP CONSTRAINT medico_pkey;
       public            postgres    false    227            �           2606    27747    paciente paciente_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (idpaciente);
 @   ALTER TABLE ONLY public.paciente DROP CONSTRAINT paciente_pkey;
       public            postgres    false    231            �           2606    27675    suministro suministro_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.suministro
    ADD CONSTRAINT suministro_pkey PRIMARY KEY (idsuministro);
 D   ALTER TABLE ONLY public.suministro DROP CONSTRAINT suministro_pkey;
       public            postgres    false    221            �           2606    27652    usuario usuario_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (idusuario);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    215            �           2606    27654    usuario usuario_usuario_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_usuario_key UNIQUE (usuario);
 E   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_usuario_key;
       public            postgres    false    215            �           2620    27788    bodeguero bitacora    TRIGGER     ~   CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.bodeguero FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 +   DROP TRIGGER bitacora ON public.bodeguero;
       public          postgres    false    225    235            �           2620    27790    enfermedad bitacora    TRIGGER        CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.enfermedad FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 ,   DROP TRIGGER bitacora ON public.enfermedad;
       public          postgres    false    235    229            �           2620    27784    especialidad bitacora    TRIGGER     �   CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.especialidad FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 .   DROP TRIGGER bitacora ON public.especialidad;
       public          postgres    false    217    235            �           2620    27792    historialmedico bitacora    TRIGGER     �   CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.historialmedico FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 1   DROP TRIGGER bitacora ON public.historialmedico;
       public          postgres    false    235    233            �           2620    27787    inventario bitacora    TRIGGER        CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.inventario FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 ,   DROP TRIGGER bitacora ON public.inventario;
       public          postgres    false    235    223            �           2620    27785    lugarmedico bitacora    TRIGGER     �   CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.lugarmedico FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 -   DROP TRIGGER bitacora ON public.lugarmedico;
       public          postgres    false    219    235            �           2620    27789    medico bitacora    TRIGGER     {   CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.medico FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 (   DROP TRIGGER bitacora ON public.medico;
       public          postgres    false    227    235            �           2620    27791    paciente bitacora    TRIGGER     }   CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.paciente FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 *   DROP TRIGGER bitacora ON public.paciente;
       public          postgres    false    235    231            �           2620    27786    suministro bitacora    TRIGGER        CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.suministro FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 ,   DROP TRIGGER bitacora ON public.suministro;
       public          postgres    false    221    235            �           2620    27783    usuario bitacora    TRIGGER     |   CREATE TRIGGER bitacora AFTER INSERT OR UPDATE ON public.usuario FOR EACH ROW EXECUTE FUNCTION public.registrar_bitacora();
 )   DROP TRIGGER bitacora ON public.usuario;
       public          postgres    false    215    235            �           2606    27705 &   bodeguero bodeguero_idlugarmedico_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.bodeguero
    ADD CONSTRAINT bodeguero_idlugarmedico_fkey FOREIGN KEY (idlugarmedico) REFERENCES public.lugarmedico(idlugarmedico);
 P   ALTER TABLE ONLY public.bodeguero DROP CONSTRAINT bodeguero_idlugarmedico_fkey;
       public          postgres    false    225    219    3240            �           2606    27700 "   bodeguero bodeguero_idusuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.bodeguero
    ADD CONSTRAINT bodeguero_idusuario_fkey FOREIGN KEY (idusuario) REFERENCES public.usuario(idusuario);
 L   ALTER TABLE ONLY public.bodeguero DROP CONSTRAINT bodeguero_idusuario_fkey;
       public          postgres    false    215    3234    225            �           2606    27767 1   historialmedico historialmedico_idenfermedad_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.historialmedico
    ADD CONSTRAINT historialmedico_idenfermedad_fkey FOREIGN KEY (idenfermedad) REFERENCES public.enfermedad(idenfermedad);
 [   ALTER TABLE ONLY public.historialmedico DROP CONSTRAINT historialmedico_idenfermedad_fkey;
       public          postgres    false    233    3250    229            �           2606    27757 2   historialmedico historialmedico_idlugarmedico_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.historialmedico
    ADD CONSTRAINT historialmedico_idlugarmedico_fkey FOREIGN KEY (idlugarmedico) REFERENCES public.lugarmedico(idlugarmedico);
 \   ALTER TABLE ONLY public.historialmedico DROP CONSTRAINT historialmedico_idlugarmedico_fkey;
       public          postgres    false    3240    233    219            �           2606    27772 -   historialmedico historialmedico_idmedico_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.historialmedico
    ADD CONSTRAINT historialmedico_idmedico_fkey FOREIGN KEY (idmedico) REFERENCES public.medico(idmedico);
 W   ALTER TABLE ONLY public.historialmedico DROP CONSTRAINT historialmedico_idmedico_fkey;
       public          postgres    false    233    3248    227            �           2606    27762 /   historialmedico historialmedico_idpaciente_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.historialmedico
    ADD CONSTRAINT historialmedico_idpaciente_fkey FOREIGN KEY (idpaciente) REFERENCES public.paciente(idpaciente);
 Y   ALTER TABLE ONLY public.historialmedico DROP CONSTRAINT historialmedico_idpaciente_fkey;
       public          postgres    false    3252    233    231            �           2606    27683 (   inventario inventario_idlugarmedico_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_idlugarmedico_fkey FOREIGN KEY (idlugarmedico) REFERENCES public.lugarmedico(idlugarmedico);
 R   ALTER TABLE ONLY public.inventario DROP CONSTRAINT inventario_idlugarmedico_fkey;
       public          postgres    false    219    223    3240            �           2606    27688 '   inventario inventario_idsuministro_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventario
    ADD CONSTRAINT inventario_idsuministro_fkey FOREIGN KEY (idsuministro) REFERENCES public.suministro(idsuministro);
 Q   ALTER TABLE ONLY public.inventario DROP CONSTRAINT inventario_idsuministro_fkey;
       public          postgres    false    3242    221    223            �           2606    27722 !   medico medico_idespecialidad_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_idespecialidad_fkey FOREIGN KEY (idespecialidad) REFERENCES public.especialidad(idespecialidad);
 K   ALTER TABLE ONLY public.medico DROP CONSTRAINT medico_idespecialidad_fkey;
       public          postgres    false    217    3238    227            �           2606    27727     medico medico_idlugarmedico_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_idlugarmedico_fkey FOREIGN KEY (idlugarmedico) REFERENCES public.lugarmedico(idlugarmedico);
 J   ALTER TABLE ONLY public.medico DROP CONSTRAINT medico_idlugarmedico_fkey;
       public          postgres    false    227    3240    219            �           2606    27717    medico medico_idusuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_idusuario_fkey FOREIGN KEY (idusuario) REFERENCES public.usuario(idusuario);
 F   ALTER TABLE ONLY public.medico DROP CONSTRAINT medico_idusuario_fkey;
       public          postgres    false    215    3234    227            n   �  x�uR�n�0<�_!��X	|-��Q�bmr˅�Ǌk��C~+���R.bĢ�>fvvv�d�*箖H�2�Uپ�>��ݏ��Evá�M��??������~��T�������#X� ,7��q�������M\HI	�|&�h@Y����������}���n�Hu�x�t)�`q�_׀N)�Z s�C1aS5b���oW��##�6$�*�����}7!��2�S_5)>�|��xn�$j_�}���濤�f,:a�pV�RE�J�KΨ���C��vy��O���쐰�i ������d�t�C;�$M-O�.�r���6)&���*�g��_�^�����)��K���u%�@ZGq�3�W����GL`J�T�x;�bJ�tE���4!MŸ_�'Zq��^��}D��Z���w�$�I�?-籚�f� "s      e   )   x�3��*M�S8��(��ӘӐˈ�� ���Ȍ���� ���      i   2   x�3�t�LLJ-I-�2���,H-*I�+�<�9�˘���¼��"�=... 2e�      ]   7   x�3�tN,J����O?�6�ˈ�%�(7��7��K--��LP��)6CQ���� ��#      m   �   x�=�M
�0��/��"��b��Ҟ���6Ѥ���<�s(E�ͼ����U�QV���Br���LˋJ��O��A^��p��'Hf
q�
�v���9D�}-\����*��8:���G�[��j�?!�đ���Z��	lmu<*����cj4l      c   8   x����0�7�➁:�d�9��+���+�aZ�M�ǃ ��~�W�!��!y DF	�      _   y   x���-A@aݞ��x���� ��4L�$�K��[q
.����y8N�[�Y� &�*�
�ɥ\0@��DM���h���ƴ��ȭ}�U�/��FJ��U�����+9aZ��T���+D� �,?>      g   ]   x�3�t)�S�*M�S>�0/9#���91''U���DA��̜���T����f�F���F\F�Y@M��e霦�&&�fF�����`�=... h�      k   �   x����0�OфY�RZ`$nFG�߶LCI��������n7�]�3��M��~F�����;⦬xV	�����ѐF�Jw��)'�e}��:P��\������Z@VM�����K��eU@o�6�}K)E&a)��D�J�\A�>�~!v�3ƾ�60�      a   3   x�3�H,JLN-I����2��L*-(�OK���2�t,.�,��K����� 41      [   M   x�3�,-.M,��7�L��+)J,N=�1ѐӀ�&c�,c�i�e�1F�1�4�2��*M̃�\���@&��1z\\\ ��$W     